'''
This program is free software: you can redistribute it and/or modify
t under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
	    
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
			    
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

import sys
import serial
import numpy as np

import Config

def build_grid_wall(x, y):
   grid = np.random.randint(255, size=((x * Config.WIDTH, (y * Config.HEIGHT) + Config.WIDTH)))
   return grid

def build_grid(x, y):
    grid = np.random.randint(255, size=( x * Config.WIDTH, y * Config.HEIGHT))
    return grid
 
def build_wall_bricklist(x ,y, fig):
   brick_list = list()
   for i in range(x):
        for j in range(y):
           brick_list.append(get_wall_brick(i, j, fig))
   return brick_list
      
def build_bricklist(x, y, fig):
    brick_list = list()
    for i in range(x):
         for j in range(y):
            brick_list.append(get_brick(i, j, fig))
    return brick_list
    
def get_wall_brick(x, y, g):
    if (x % 2):
       row_ini = (x * Config.WIDTH)
       row_end = ((x + 1) * Config.WIDTH)
       col_ini = ((y * Config.HEIGHT) + Config.WIDTH)
       col_end = (((y + 1) * Config.HEIGHT) + Config.WIDTH)
       b = g[row_ini:row_end, col_ini:col_end]
       return b       
    else:
       row_ini = (x * Config.WIDTH)
       row_end = ((x + 1) * Config.WIDTH)
       col_ini = (y * Config.HEIGHT)
       col_end = ((y + 1) * Config.HEIGHT)
       b = g[row_ini:row_end, col_ini:col_end]
       return b
       

def get_brick(x, y, g):
    row_ini = (x * Config.WIDTH)
    row_end = ((x + 1) * Config.WIDTH)
    col_ini = (y * Config.HEIGHT)
    col_end = ((y + 1) * Config.HEIGHT)
    b = g[row_ini:row_end, col_ini:col_end]
    return b

def swap_column(b):
    swap_table = [0, 8, 1, 9, 2, 3, 10, 4, 5, 11, 6, 7, 12, 14, 15, 13, 16, 18, 19, 17, 20, 24, 25, 21, 26, 27, 22, 28, 29, 23, 30, 31]
    #swap_table = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31] 
    new_brick = np.zeros((Config.WIDTH, Config.HEIGHT)) #np.zeros((16, 32), dtype='int8')
    for j in range(Config.HEIGHT):
        for i in range(Config.WIDTH):
            new_brick[(i, j)] = b[(i, swap_table[j])]
    return new_brick

def sendserial(b_list, s):
    i = 0
    if (not s.isOpen()):
       sys.exit('cannot open the serial port')
    for brick in b_list:
       s.write("T")
       #print i
       s.write(chr(Config.ADDR_LIST[i]))
       i = i + 1
       b = swap_column(brick)
       b = b.reshape(1,512)
       bbytes = np.zeros((1,64), dtype='uint8')
       count = 0
       for led in range(512):  
          if(b[0,led] > 128):
             bbytes[0,led/8] |= (0x80>>(led%8))
       for led in range(64):
          if ((led%8) == 0):
             s.write(chr(count)) 
             count = count + 8  
          s.write(chr(bbytes[0,led]))
       s.write("\n")
       s.write("P")     
       #print s.read(1)
       print s.readline()
    s.write("Z")     
    
def writetofile(b_list):
   fp = open("data.hex","w")
   for brick in b_list:
      b = swap_column(brick)
      b = b.reshape(1,512)
      bbytes = np.zeros((1,64), dtype='uint8')
      count = 0
      for led in range(512):  
         if(b[0,led] < 128):
            bbytes[0,led/8] |= (0x80>>(led%8))
      print "#ifdef PIC\n", "uint8_t picture[] PROGMEM={",
      for led in range(64):
         if ((led%8) == 0):
            fp.write(chr(count)) 
            count = count + 8
            print
         print hex(bbytes[0,led]),", ",
         fp.write(chr(bbytes[0,led]))
         #print
      print "};\n","#endif"
      fp.write("\n")
   print
   fp.close()
      
