import time
import datetime 
import colorsys
import threading as th
import sys

import ledmatrix

loop_active = True

def key_capture_thread(): 
    global loop_active
    print("ïk ga wachten") 
    input()
    loop_active = False
    print('ïk kap ermee')
th.Thread(target=key_capture_thread, args=(), name='stop', daemon=True).start()


WIDTH = 14
HEIGHT = 14

from PIL import Image
regenboog = Image.open("images/regenboog.png")
regenboog = regenboog.resize((14,14))

pacman_7_7_l = [ Image.open("images/pekmen_0.png"), Image.open("images/pekmen_links.png") ]
pacman_7_7_r = [ Image.open("images/pekmen_0.png"), Image.open("images/pekmen_rechts.png") ]
spook_paars_7_7 = [ Image.open("images/spook_paars_0.png"), Image.open("images/spook_paars_1.png") ]


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


    

led_matrix = ledmatrix.ledmatrix()

# scroll all numbers
# pos = WIDTH
# while(pos > -10 *(number_width + 1 )): 
#     offset = 0
#     led_matrix.clear_screen()
#     for n in range(10) :
#         led_matrix.set_image(pos + offset, 0, im_number[n])
#         offset += number_width + 1
#     led_matrix.set_show()
#     #time.sleep(0.01)
#     pos -= 1
    

last_FPS_time_s = time.time()
last_pacmen_time_s = time.time()
frames = 0
pacman_min_pos = -16
pacman_hour_pos = 16
last_minute = datetime.datetime.now().minute
last_hour = datetime.datetime.now().hour
pacman_min_active = False
pacman_hour_active = False
while(loop_active):
    frames += 1
    now = datetime.datetime.now()    # print now.year, now.month, now.day, now.hour, now.minute, now.second
    cur_hour_str = str(now.hour).zfill(2)
    cur_minu_str = str(now.minute).zfill(2)

    hsv_h = (time.time() % 10) /10
    led_matrix.clear_screen()

    # fill background
    rgb_back = colorsys.hsv_to_rgb((hsv_h + 0.5)%1, 1, 0.1)
    rgb_back = (255*rgb_back[0], 255*rgb_back[1], 255*rgb_back[2])
    led_matrix.fill_screen(rgb_back)

    # display time
    rgb = colorsys.hsv_to_rgb(hsv_h, 1, 1)
    rgb = (255*rgb[0], 255*rgb[1], 255*rgb[2])
    led_matrix.set_image(1, 0, im_number[int(cur_hour_str[0])], rgb)
    led_matrix.set_image(5, 0, im_number[int(cur_hour_str[1])], rgb)

    led_matrix.set_image(6, 7, im_number[int(cur_minu_str[0])], rgb)
    led_matrix.set_image(10, 7, im_number[int(cur_minu_str[1])], rgb)


    if(pacman_min_active):
        led_matrix.set_image(pacman_min_pos, 7, pacman_7_7_r[int(pacman_min_pos % 2)] )
        led_matrix.set_image(pacman_min_pos + 9, 7, spook_paars_7_7[int(pacman_min_pos % 2)] )

    if(pacman_hour_active):
        led_matrix.set_image(pacman_hour_pos, 0, spook_paars_7_7[int(pacman_hour_pos % 2)] )
        led_matrix.set_image(pacman_hour_pos + 9, 0, pacman_7_7_l[int(pacman_hour_pos % 2)] )


    led_matrix.set_show()

    if time.time() > last_FPS_time_s + 1 :
        #print(f'FPS {frames}')
        frames = 0
        last_FPS_time_s = time.time()
        
    if (time.time() > last_pacmen_time_s + 0.25):
        if pacman_min_active :
            pacman_min_pos += 1
            if (pacman_min_pos > 16): 
                pacman_min_pos = -16
                pacman_min_active = False
        if pacman_hour_active :
            pacman_hour_pos -= 1
            if (pacman_hour_pos < -16): 
                pacman_hour_pos = 16
                pacman_hour_active = False
        last_pacmen_time_s = time.time()

    if (now.minute != last_minute ) :
        pacman_min_active = True
        last_minute = now.minute
    if (now.hour != last_hour ) :
        pacman_hour_active = True
        last_hour = now.hour

    



