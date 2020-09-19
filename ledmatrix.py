import math, time

import board
import neopixel

class ledmatrix:
    def __init__(self, pixel_encoding="RGB", height=14, width=14):
        self._height = height
        self._width = width
        self._total_length = height*width
        self._neopixel =  neopixel.NeoPixel(board.D18, self._total_length, auto_write=False, pixel_order=pixel_encoding)
        for i in range(0, self._total_length):
            self._neopixel[i] = (255,255,255)
        self._neopixel.show()
        time.sleep(0.1)

    def set_show(self) : 
        self._neopixel.show()

    def clear_screen(self):
        for i in range(0, self._total_length):
            self._neopixel[i] = (0,0,0)

    def fill_screen(self, color):
        for i in range(0, self._total_length):
            self._neopixel[i] = color

    def set_pixel(self, x, y, color):
        self.__set_pixel(x, y, color)


    def set_image(self, x, y, image, color=None):
        size_x = min(image.width, self._width - x)
        size_y = min(image.height, self._height - y)
        for xx in range(0, size_x):
            for yy in range(0, size_y):
                if color == None :
                    c = image.getpixel((xx, yy))[:3]
                    self.__set_pixel(x+xx, y+yy, c)
                else : 
                    if image.getpixel((xx, yy))[:3] != (0,0,0) :
                        c = color
                        self.__set_pixel(x+xx, y+yy, c)
                    #else :
                    #    c = (0,0,0) 
                

    def __set_pixel(self, x, y, color):
        if (x >= 0) and (x < self._width) and (y >= 0) and (y < self._height) :
            i = self.calculate_index(x, y)
            self._neopixel[i] = color

    def calculate_index(self, x, y):
        row = self._height - y
        invert_row = (row%2 == 0)
        if invert_row:
            x = self._width - 1 - x
        return self._total_length - 1 - x - (y*self._width)
