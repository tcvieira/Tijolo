#!/usr/bin/env python
# -*- coding: latin1 -*-

import Bricks
import Figure
import sys
import argparse

#constantes
width = 16
height = 32
brick_list = list()

# variaveis de entrada
x = int(sys.argv[1]) #quantidade de tijolos no eixo x
y = int(sys.argv[2]) #quantidade de tijolos no eixo y

fig_width = x * width	
fig_height = y * height
fig = Figure.build_image(sys.argv[3], x, y)
figarray = Figure.build_imarray(fig, x, y)
for i in range(x):
   for j in range(y):
      brick_list.append(Bricks.get_brick(i, j, figarray))
for brick in brick_list:
   print brick
#send_matrix_serial(brick_list)








   

