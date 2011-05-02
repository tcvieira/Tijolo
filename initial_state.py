#!/usr/bin/python
import sys
import numpy
import random

matrix = [[[None] for col in range(32)] for row in range(16)]
print matrix,"\n"
#fp = open(sys.argv[1], "w")
for i in range(16):
   for j in range(32):
      matrix[i][j] = random.randint(0,1)
for row in matrix:
   print row,"\n"

   
   