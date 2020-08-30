import math, time

import board
import neopixel

class ledmatrix:
    def __init__(self, pixel_encoding="RGB", height=14, width=14):
        self._height = height
        self._width = width
        self._total_length = height*width
        self._neopixel =  neopixel.NeoPixel(board.D18, self._total_length, auto_write=False, pixel_order=pixel_encoding)
        self._neopixel[0] = (255,0,0)
        self._neopixel.show()
        time.sleep(1)
        
        

    def set_pixel(self, x, y, color):
        self.__set_pixel(x, y, color)
        self._neopixel.show()


    def set_image(self, x, y, image):
        size_x = min(image.width, self._width - x)
        size_y = min(image.height, self._height - y)
        for xx in range(0, size_x):
            for yy in range(0, size_y):
                self.__set_pixel(x+xx, y+yy, image.getpixel((xx, yy))[:3])
        self._neopixel.show()

    def __set_pixel(self, x, y, color):
        i = self.calculate_index(x, y)
        self._neopixel[i] = color

    def calculate_index(self, x, y):
        row = self._height - y
        invert_row = (row%2 == 0)
        if invert_row:
            x = self._width - 1 - x
        return self._total_length - 1 - x - (y*self._width)
