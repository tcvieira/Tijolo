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

import random
import Bricks
import Config

def update_wall(grid, x, y, geracao):
   if (get_total(grid,x,y) < 30 or not(geracao % 300)):
      return Bricks.build_grid_wall(x, y)
   updated_grid = Bricks.build_grid_wall(x, y)
   for i in range(Config.WIDTH * x):
      for j in range((Config.HEIGHT * y) + Config.WIDTH):
         neighbors = get_neighbors(i, j, Config.WIDTH * x, (Config.HEIGHT * y) + Config.WIDTH, grid)
         if(get_cell(i, j, Config.WIDTH * x, (Config.HEIGHT * y) + Config.WIDTH, grid)):
            if(neighbors < 2):
               updated_grid[i,j] = Config.DEAD
            elif(neighbors > 3):
               updated_grid[i,j] = Config.DEAD
            else:
               updated_grid[i,j] = Config.LIVE
         else:
            if(neighbors == 3):
               updated_grid[i,j] = Config.LIVE
            else:
               updated_grid[i,j] = Config.DEAD
   return updated_grid
   

def update(grid, x, y, geracao):
   if (get_total(grid,x,y) < 30 or not(geracao % 300)):
         return Bricks.build_grid(x, y)      
   updated_grid = Bricks.build_grid(x, y)
   for i in range(Config.WIDTH * x):
      for j in range(Config.HEIGHT * y):
         neighbors = get_neighbors(i, j, Config.WIDTH * x, Config.HEIGHT * y, grid)
         if(get_cell(i, j, Config.WIDTH * x, Config.HEIGHT * y, grid)):
            if(neighbors < 2):
               updated_grid[i,j] = Config.DEAD
            elif(neighbors > 3):
               updated_grid[i,j] = Config.DEAD
            else:
               updated_grid[i,j] = Config.LIVE
         else:
            if(neighbors == 3):
               updated_grid[i,j] = Config.LIVE
            else:
               updated_grid[i,j] = Config.DEAD
   return updated_grid
   
def get_total(grid,x,y):
   count = 0
   for i in range(Config.WIDTH * x):
      for j in range(Config.HEIGHT * y):
         if (get_cell(i, j, Config.WIDTH * x, Config.HEIGHT * y, grid)):
            count = count + 1
   print "LIVE ",count
   return count   
   
def get_cell(x, y, x_max, y_max, g):
   if(x < 0 or x >= x_max or y < 0 or y >= y_max):
      return 0
   else:
      if(g[x,y] < 128):
         return 1
      else:
         return 0


def get_neighbors(x,y,x_max,y_max,g):
   out = 0
   if(get_cell(x-1,y-1,x_max,y_max,g)):
      out = out + 1
   if(get_cell(x-1,y,x_max,y_max,g)):
      out = out + 1
   if(get_cell(x-1,y+1,x_max,y_max,g)):
      out = out + 1
      
   if(get_cell(x,y-1,x_max,y_max,g)):
      out = out + 1
   if(get_cell(x,y+1,x_max,y_max,g)):
      out = out + 1
      
   if(get_cell(x+1,y-1,x_max,y_max,g)):
      out = out + 1
   if(get_cell(x+1,y,x_max,y_max,g)):
      out = out + 1
   if(get_cell(x+1,y+1,x_max,y_max,g)):
      out = out + 1
      
   return out

