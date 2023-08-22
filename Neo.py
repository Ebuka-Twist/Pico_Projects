import machine
import neopixel
import utime

# Configuration for WS2812
NUM_LEDS = 30
PIN_NUM = 2  # Pin number on Raspberry Pi Pico

# Create a neopixel object
pixels = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_LEDS)

def running_light_animation(duration=5):
    start_time = utime()
    while utime() - start_time < duration:
        for i in range(NUM_LEDS):
            pixels.fill((0, 0, 0))
            pixels[i] = (0, 0, 255)  # Blue color
            pixels.write()
            utime.sleep(10)
        for i in range(NUM_LEDS - 1, -1, -1):
            pixels.fill((0, 0, 0))
            pixels[i] = (0, 0, 255)  # Blue color
            pixels.write()
            utime.sleep(10)

# Start the animation

try:
    while True:
        running_light_animation()
    
except KeyboardInterrupt:
    pass    
        
        
        