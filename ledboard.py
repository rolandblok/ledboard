import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 14*14) # Raspberry Pi wiring!
pixels[0] = (255, 0, 0)
