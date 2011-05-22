#!/usr/bin/env python
# -*- coding: latin1 -*-

from PIL import Image
import Bricks

width = 16
height = 32

def build_image(figure, x, y):
   im = Image.open(figure)	#imagem para ser convertida ( TODO: ajustar para receber uma lista de imagens ou uma pasta com imagens)
   print im.format, im.size, im.info
   im.show()
   # convert to black white
   fig = im.convert("L").rotate(90) #ainda é preciso rotacionar ?!?! VERIFICAR
   #fig.show()
   fig = fig.resize((x * width, y * height))
   #fig.show()
   return fig

def build_imarray(im, x, y):
   imarray = Bricks.build_grid(x, y)
   pixels = im.load()
   for i in range(x * width):
   	for j in range(y * height):
   		imarray[i,j] = pixels[i,j] # load method is faster than getpixel: im.getpixel((i,j))
   return imarray


