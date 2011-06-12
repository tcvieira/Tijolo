#!/usr/bin/env python
# -*- coding: latin1 -*-

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

import glob
import optparse
import serial
import time
import Bricks
import Figure
import GameOfLife
import Config

brick_list = list()
fig_list = list()

usage = "usage: %prog -x <width> -y <height> -m <mode> -f <image folder>"
optParser = optparse.OptionParser(usage=usage)
optParser.add_option("-x", "--width", action="store", dest="x", metavar="width", type="int", help="# of brick in x axe")
optParser.add_option("-y", "--height", action="store", dest="y", metavar="height", type="int", help="# of brick in y axe")
optParser.add_option("-m", "--mode", action="store", dest="mode", type="choice", choices=["gol", "im", "hib", "rand"], help="mode := gol = gameoflife | im = images | hib = hibrid")
optParser.add_option("-w", "--wall", action="store_true", dest="wall", default=False, metavar="wall", help="# of brick in x axe")
optParser.add_option("-f", "--folder", action="store", dest= "folder", type="string", help="name of the folder containing the images")
options, remainingArgs = optParser.parse_args()

if (options.mode == "rand"):
   print "TODO"

elif (options.mode == "im"):
   listing = glob.glob(options.folder)
   #print fig_list
   s = serial.Serial(Config.SERIAL_PORT, Config.SERIAL_BAUD_RATE, dsrdtr=True)
   s.open()
   if not options.wall:
      for infile in listing:       
         fig = Figure.build_image(infile, options.x, options.y, options.wall)
         figarray = Figure.build_imarray(fig, options.x, options.y, options.wall)
         brick_list = Bricks.build_bricklist(options.x, options.y,figarray)
         fig_list.append(brick_list)
      turn = 0
      while True:
      #if (True):
         for fig in fig_list:
            #Bricks.writetofile(fig)
            Bricks.sendserial(fig, s)
            turn = turn + 1
            print turn
            time.sleep(0.1)
   else:
       print "modo wall"
       for infile in listing:       
          fig = Figure.build_image(infile, options.x, options.y, options.wall)
          figarray = Figure.build_imarray(fig, options.x, options.y, options.wall)
          brick_list = Bricks.build_wall_bricklist(options.x, options.y,figarray)
          fig_list.append(brick_list)
       turn = 0
       while True:
       #if (True):
          for fig in fig_list:
             #Bricks.writetofile(fig)
             Bricks.sendserial(fig, s)
             turn = turn + 1
             print turn
             time.sleep(0.1)
   s.close()
   
elif (options.mode == "gol"):
   #s = serial.Serial('/dev/ttyS0', 115200)
   s = serial.Serial(Config.SERIAL_PORT, Config.SERIAL_BAUD_RATE, dsrdtr=True)
   s.open()
   turn = 0
   if not options.wall:
       grid = Bricks.build_grid(options.x, options.y)
       while True:
          brick_list = Bricks.build_bricklist(options.x, options.y, grid)
          Bricks.sendserial(brick_list,s)
          turn = turn + 1
          print "geracao ", turn
          time.sleep(0.05)
          grid = GameOfLife.update(grid, options.x, options.y, turn)
   else:
       print "modo wall"
       grid = Bricks.build_grid_wall(options.x, options.y)
       while True:
          brick_list = Bricks.build_wall_bricklist(options.x, options.y, grid)
          Bricks.sendserial(brick_list,s)
          turn = turn + 1
          print "geracao ", turn
          time.sleep(0.05)
          grid = GameOfLife.update_wall(grid, options.x, options.y, turn)
   s.close()
   
elif (options.mode == "hib"):
   listing = glob.glob(options.folder)
   for infile in listing:       
      fig = Figure.build_image(infile, options.x, options.y)
      figarray = Figure.build_imarray(fig, options.x, options.y)
      brick_list = Bricks.build_bricklist(options.x, options.y, figarray)
      #fig_list.append(brick_list)
   s = serial.Serial(Config.SERIAL_PORT, Config.SERIAL_BAUD_RATE, dsrdtr=True)
   s.open()
   turn = 0
   if not options.wall:
       while True:
          Bricks.sendserial(brick_list,s)
          #raw_input()
          brick_list = list()
          time.sleep(0.05)
          figarray = GameOfLife.update(figarray, options.x, options.y, turn)
          for i in range(options.x):
             for j in range(options.y):
                brick_list.append(Bricks.get_brick(i, j, figarray))
          turn = turn + 1
          print "geracao ",   turn
   else:
       print "modo wall"
   s.close()
   
else:
   print "mode not available, try Tijolo.py -h for help" + usage
 

