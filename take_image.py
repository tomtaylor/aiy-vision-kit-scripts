#!/usr/bin/env python3
"""Take a photo with the timestamp in the filename, every time the button is
pressed.
"""
from gpiozero import Button
from aiy.pins import BUTTON_GPIO_PIN
from picamera import PiCamera
import time

# Set up a gpiozero Button using the button included with the vision hat.
button = Button(BUTTON_GPIO_PIN)

while True:
    with PiCamera() as camera:
        camera.resolution = (1640, 922)  # Full Frame, 16:9 

        if button.is_pressed:
            i = int(time.time()) 
            name = 'image-{}.jpg'.format(i)
            print("Capturing {}".format(name))
            camera.capture(name)
