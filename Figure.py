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

from PIL import Image
import Bricks
import Config


def build_image(figure, x, y, wall):
   im = Image.open(figure)	#imagem para ser convertida ( TODO: ajustar para receber uma lista de imagens ou uma pasta com imagens)
   print im.format, im.size, im.info
   #im.show()
   # convert to black white
   fig = im.convert("L").transpose(Image.FLIP_LEFT_RIGHT).rotate(90)
   if wall:
      fig = fig.resize((x * Config.WIDTH, (y * Config.HEIGHT) + Config.WIDTH))
   else:
      fig = fig.resize((x * Config.WIDTH, y * Config.HEIGHT))  
   return fig

def build_imarray(im, x, y, wall):
   if wall:
      imarray = Bricks.build_grid_wall(x, y)
      pixels = im.load()
      for i in range(x * Config.WIDTH):
      	for j in range((y * Config.HEIGHT) + Config.WIDTH):
      		imarray[i,j] = pixels[i,j] # load method is faster than getpixel: im.getpixel((i,j))
      return imarray
   else:
      imarray = Bricks.build_grid(x, y)
      pixels = im.load()
      for i in range(x * Config.WIDTH):
      	for j in range(y * Config.HEIGHT):
      		imarray[i,j] = pixels[i,j] # load method is faster than getpixel: im.getpixel((i,j))
   return imarray


