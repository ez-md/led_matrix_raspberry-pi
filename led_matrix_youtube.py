#!/usr/bin/env python3


import RPi.GPIO as GPIO
from time import sleep, strftime
from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT, TINY_FONT, SINCLAIR_FONT

import urllib.request 
import json



serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)
virtual = viewport(device, width=32, height=16)

def get_subs():

    name="<YOUTUBE CHANNEL ID>"
    key="API KEY"
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key="+key).read()
    subs=json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    with canvas(device) as draw:
#       ss=text(draw,(0, 1),subs, fill="White", font=proportional(CP437_FONT))
        ss=text(draw,(0, 1),subs, fill="White",)
        return ss


def welcome_message():
    wc_message = show_message(device, 'As-salamu alaykum', fill="White", font=proportional(LCD_FONT), scroll_delay=0.03)
    return wc_message


def show_time():
    with canvas(virtual) as draw:
        time = text(draw,(0 ,1), datetime.now().strftime('%-I:%M'), fill="white", font=proportional(CP437_FONT))
        return time



def show_solo():
    solo = show_message(device, 'Solo Z Rider    Solo Z Rider', fill="White", scroll_delay=0.03)
#    solo = show_message(device, 'Solo Z Rider    Solo Z Rider', fill="White", font=proportional(CP437_FONT), scroll_delay=0.03)
    return solo






def main():
    welcome_message()
    try:
        while True:
            device.contrast(1)
            show_time()
            sleep(15)
            show_solo()
            get_subs()
            sleep(5)
    
    except KeyboardInterrupt:
            GPIO.cleanup()

if __name__ == '__main__':
    main()
