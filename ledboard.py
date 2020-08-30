import time

from PIL import Image
regenboog = Image.open("regenboog.png")
regenboog = regenboog.resize((14,14))

pacmanmonddicht = Image.open("pacman mond dicht.png")
pacmanmondopen = Image.open("pacman mond open.png")
spb = Image.open("spook blauw.png")
spr = Image.open("spook rood.png")


import ledmatrix
m = ledmatrix.ledmatrix()

while(True):
    m.set_image(0, 0, pacmanmonddicht)
    time.sleep(1)
    m.set_image(0, 0, pacmanmondopen)
    time.sleep(1)
    m.set_image(0, 0, spb)
    time.sleep(1)
    m.set_image(0, 0, spr)
    time.sleep(1)