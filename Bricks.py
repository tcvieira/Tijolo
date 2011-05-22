import numpy as np
import sys
width = 16
height = 32

def build_grid(x, y):
    grid = np.random.randint(2, size=((x * width), (y * height)))
    grid.dtype = 'int8'
    return grid

def get_brick(x, y, g):
    row_ini = (x * width)
    row_end = ((x + 1) * width)
    col_ini = (y * height)
    col_end = ((y + 1) * height)
    b = g[(row_ini:row_end, col_ini:col_end)]
    return b

def swap_column(b):
    swap_table = [0, 2, 4, 5, 7, 8, 10, 11, 1, 3, 6, 9, 12, 15, 13, 14, 16, 19, 17, 18, 20, 23, 26, 29, 21, 22, 24, 25, 27, 28, 30, 31]
    new_brick = np.zeros((16, 32), dtype='int8')
    for j in range(height):
        for i in range(width):
            new_brick[(i, j)] = b[(i, swap_table[j])]
    return new_brick

def send_matrix_serial(b_list):
    s = serial.Serial('/dev/ttyS1', 115200)
    s.open()
    if (not s.isOpen()):
       sys.exit('cannot open the serial port'))
    for brick in b_list:
        swap_column(brick)
        for led in brick.flat:
            s.write(led)


    s.close