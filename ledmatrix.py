import math

import board
import neopixel

class ledmatrix:
    def __init__(self, pixel_encoding="GRB", height=14, width=14):
        self._height = height
        self._width = width
        self._total_length = height*width
        self._neopixel =  neopixel.NeoPixel(board.D18, self._total_length)

    def set_pixel(self, x, y, color):
        i = self.calculate_index(x, y)
        self._neopixel[i] = color

    def set_image(self, x, y, image):
        size_x = math.max(image.width, self._width - x)
        size_y = math.max(image.height, self._height - y)
        for xx in range(0, size_x):
            for yy in range(0, size_y):
                set_pixel(x+xx, y+yy, image.getpixel((xx, yy)))

    def calculate_index(self, x, y):
        row = self._height - y
        invert_row = (row%2 == 0)
        if invert_row:
            x = self._width - 1 - x
        return self._total_length - 1 - x - (y*self._width)
