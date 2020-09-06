import time
import datetime 

WIDTH = 14
HEIGHT = 14

from PIL import Image
regenboog = Image.open("images/regenboog.png")
regenboog = regenboog.resize((14,14))

pacmanmonddicht = Image.open("images/pacman mond dicht.png")
pacmanmondopen = Image.open("images/pacman mond open.png")
spb = Image.open("images/spook blauw.png")
spr = Image.open("images/spook rood.png")

im_number = [0 for i in range(10)]
im_number[0] = Image.open("images/0.png")
im_number[1] = Image.open("images/1.png")
im_number[2] = Image.open("images/2.png")
im_number[3] = Image.open("images/3.png")
im_number[4] = Image.open("images/4.png")
im_number[5] = Image.open("images/5.png")
im_number[6] = Image.open("images/6.png")
im_number[7] = Image.open("images/7.png")
im_number[8] = Image.open("images/8.png")
im_number[9] = Image.open("images/9.png")
im_dd        = Image.open("images/dd.png")
number_width = 3 
number_height = 6 


    

import ledmatrix
led_matrix = ledmatrix.ledmatrix()

# scroll all numbers
pos = WIDTH
while(pos > -10 *(number_width + 1 )): 
    offset = 0
    led_matrix.clear_screen()
    for n in range(10) :
        led_matrix.set_image(pos + offset, 0, im_number[n])
        offset += number_width + 1
    led_matrix.set_show()
    time.sleep(0.04)
    pos -= 1

led_matrix.set_image(0, 0, pacmanmonddicht)
led_matrix.set_show()
time.sleep(1)
led_matrix.set_image(0, 0, pacmanmondopen)
led_matrix.set_show()
time.sleep(1)
led_matrix.set_image(0, 0, spb)
led_matrix.set_show()
time.sleep(1)
led_matrix.set_image(0, 0, spr)
led_matrix.set_show()
time.sleep(1)

while(True):

    now = datetime.datetime.now()    # print now.year, now.month, now.day, now.hour, now.minute, now.second
    cur_hour_str = str(now.hour).zfill(2)
    cur_minu_str = str(now.minute).zfill(2)

    led_matrix.clear_screen()

    led_matrix.set_image(1, 0, im_number[int(cur_hour_str[0])])
    led_matrix.set_image(5, 0, im_number[int(cur_hour_str[1])])

    led_matrix.set_image(6, 7, im_number[int(cur_minu_str[0])])
    led_matrix.set_image(10, 7, im_number[int(cur_minu_str[1])])

    led_matrix.set_show()

    time.sleep(1)


