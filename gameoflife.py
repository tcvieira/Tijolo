#!/usr/bin/python
# -*- coding: latin1 -*-

#entrada: tamanho de cada tijolo, quantidade de tijolos e arquivo com a configuração inicial
#montar a matriz esparsa.
#loop
#checa celulas.
#gera nova matriz esparsa.
#envia.
#32X16linhas
#tentar fazer com lista[1::] a partilha

'''
pic_new[0] = pic_temp[0].copy() COLUNA 0 NA MATRIX = COLUNA 0 NA PLACA
pic_new[1] = pic_temp[8].copy() COLUNA 8 NA MATRIX = COLUNA 1 NA PLACA
pic_new[2] = pic_temp[1].copy() COLUNA 1 NA MATRIX = COLUNA 2 NA PLACA
pic_new[3] = pic_temp[9].copy() COLUNA 9 NA MATRIX = COLUNA 3 NA PLACA
pic_new[4] = pic_temp[2].copy() ...
pic_new[5] = pic_temp[3].copy()
pic_new[6] = pic_temp[10].copy()
pic_new[7] = pic_temp[4].copy()
pic_new[8] = pic_temp[5].copy()
pic_new[9] = pic_temp[11].copy()
pic_new[10] = pic_temp[6].copy()
pic_new[11] = pic_temp[7].copy()
pic_new[12] = pic_temp[12].copy()
pic_new[13] = pic_temp[14].copy()
pic_new[14] = pic_temp[15].copy()
pic_new[15] = pic_temp[13].copy()
pic_new[16] = pic_temp[16].copy()
pic_new[17] = pic_temp[18].copy()
pic_new[18] = pic_temp[19].copy()
pic_new[19] = pic_temp[17].copy()
pic_new[20] = pic_temp[20].copy()
pic_new[21] = pic_temp[24].copy()
pic_new[22] = pic_temp[25].copy()
pic_new[23] = pic_temp[21].copy()
pic_new[24] = pic_temp[26].copy()
pic_new[25] = pic_temp[27].copy()
pic_new[26] = pic_temp[22].copy()
pic_new[27] = pic_temp[28].copy()
pic_new[28] = pic_temp[29].copy()
pic_new[29] = pic_temp[23].copy()
pic_new[30] = pic_temp[30].copy()
pic_new[31] = pic_temp[31].copy() 
'''

import sys
import random

width = 16
height = 32

class gameoflife(object):

   def build_grid(size):

      grid = [[[None] for row in range(size*height)] for column in range(size*width)]
      for row in range(size*width):
         for column in range(size*height):
            grid[row][column] = random.randint(0,1)
      for row in grid:
         print row
      return grid

   def get_brick(b, g):

      #olhar opcoes do range()
      #a quantidade de iteracoes esta certa, falta alterar o ponto inicial p ela
      for i in range((b * height) - 1):
         for j in range((b * width) - 1):
            brick[r][c] = grid[i][j]

   '''   
   def update_matrix(m):

   def send_matrix_serial(list, num_tijolos):
      s = serial.Serial('/dev/ttyS1', 115200)
      s.open()
      if not s.isOpen():
         sys.exit("cannot open the serial port")
      for t in range(num_tijolos):
         package = get_tijolo(t,list)
         for item in package:
            s.write(item)
      s.close
   '''



   size = 2
   grid = build_grid(size)
   #brick = get_brick(1,grid)
