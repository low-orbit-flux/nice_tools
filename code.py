# SPDX-FileCopyrightText: 2021 Sandy Macdonald
#
# SPDX-License-Identifier: MIT

# A simple example of how to set up a keymap and HID keyboard on Keybow 2040.

# You'll need to connect Keybow 2040 to a computer, as you would with a regular
# USB keyboard.

# Drop the keybow2040.py file into your `lib` folder on your `CIRCUITPY` drive.

# NOTE! Requires the adafruit_hid CircuitPython library also!


# https://docs.circuitpython.org/projects/hid/en/latest/api.html
# keyboard.press(myKeys[i][0])
# keyboard.release(myKeys[i][0])


## heavily modified,  keeping the above comments



import board
from keybow2040 import Keybow2040

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Set up Keybow
i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys

# Set up the keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)



# The colour to set the keys when pressed, yellow.
rgb = (0, 255, 0)


myPlatform = "pc"   # mac or pc


myKeys = {
    "a": (Keycode.A,),
    "b": (Keycode.B,),
    "c": (Keycode.C,),
    "d": (Keycode.D,),
    "e": (Keycode.E,),
    "f": (Keycode.F,),
    "g": (Keycode.G,),
    "h": (Keycode.H,),
    "i": (Keycode.I,),
    "j": (Keycode.J,),
    "k": (Keycode.K,),
    "l": (Keycode.L,),
    "m": (Keycode.M,),
    "n": (Keycode.N,),
    "o": (Keycode.O,),
    "p": (Keycode.P,),
    "q": (Keycode.Q,),
    "r": (Keycode.R,),
    "s": (Keycode.S,),
    "t": (Keycode.T,),
    "u": (Keycode.U,),
    "v": (Keycode.V,),
    "w": (Keycode.W,),
    "x": (Keycode.X,),
    "y": (Keycode.Y,),
    "z": (Keycode.Z,),
    "A": (Keycode.LEFT_SHIFT, Keycode.A,),
    "B": (Keycode.LEFT_SHIFT, Keycode.B,),
    "C": (Keycode.LEFT_SHIFT, Keycode.C,),
    "D": (Keycode.LEFT_SHIFT, Keycode.D,),
    "E": (Keycode.LEFT_SHIFT, Keycode.E,),
    "F": (Keycode.LEFT_SHIFT, Keycode.F,),
    "G": (Keycode.LEFT_SHIFT, Keycode.G,),
    "H": (Keycode.LEFT_SHIFT, Keycode.H,),
    "I": (Keycode.LEFT_SHIFT, Keycode.I,),
    "J": (Keycode.LEFT_SHIFT, Keycode.J,),
    "K": (Keycode.LEFT_SHIFT, Keycode.K,),
    "L": (Keycode.LEFT_SHIFT, Keycode.L,),
    "M": (Keycode.LEFT_SHIFT, Keycode.M,),
    "N": (Keycode.LEFT_SHIFT, Keycode.N,),
    "O": (Keycode.LEFT_SHIFT, Keycode.O,),
    "P": (Keycode.LEFT_SHIFT, Keycode.P,),
    "Q": (Keycode.LEFT_SHIFT, Keycode.Q,),
    "R": (Keycode.LEFT_SHIFT, Keycode.R,),
    "S": (Keycode.LEFT_SHIFT, Keycode.S,),
    "T": (Keycode.LEFT_SHIFT, Keycode.T,),
    "U": (Keycode.LEFT_SHIFT, Keycode.U,),
    "V": (Keycode.LEFT_SHIFT, Keycode.V,),
    "W": (Keycode.LEFT_SHIFT, Keycode.W,),
    "X": (Keycode.LEFT_SHIFT, Keycode.X,),
    "Y": (Keycode.LEFT_SHIFT, Keycode.Y,),
    "Z": (Keycode.LEFT_SHIFT, Keycode.Z,),
    "0": (Keycode.ZERO,),
    "1": (Keycode.ONE,),
    "2": (Keycode.TWO,),
    "3": (Keycode.THREE,),
    "4": (Keycode.FOUR,),
    "5": (Keycode.FIVE,),
    "6": (Keycode.SIX,),
    "7": (Keycode.SEVEN,),
    "8": (Keycode.EIGHT,),
    "9": (Keycode.NINE,),
    "!": (Keycode.LEFT_SHIFT, Keycode.ONE,),
    ".": (Keycode.PERIOD,),



    "\"": (Keycode.LEFT_SHIFT, Keycode.QUOTE,),
    "&": (Keycode.LEFT_SHIFT, Keycode.SEVEN), 
    ";": (Keycode.SEMICOLON,), 
    ">": (Keycode.LEFT_SHIFT, Keycode.PERIOD,),
    "<": (Keycode.LEFT_SHIFT, Keycode.COMMA,),
    "=": (Keycode.EQUALS,),
    "-": (Keycode.KEYPAD_MINUS,),
    "/": (Keycode.KEYPAD_FORWARD_SLASH,),
    " ": (Keycode.SPACEBAR,)
    }

def mySendString(a):
    for i in a:
        if i in myKeys:
            if len(myKeys[i]) > 1:
                keyboard.send(myKeys[i][1], myKeys[i][0])

            else:
                keyboard.send(myKeys[i][0])

# Attach handler functions to all of the keys
for key in keys:
    # A press handler that sends the keycode and turns on the LED
    @keybow.on_press(key)
    def press_handler(key):

        key.set_led(*rgb)

        if(key.number == 0):
            if myPlatform == "mac":
                keyboard.send(Keycode.GUI, Keycode.C)
            else:
                keyboard.send(Keycode.LEFT_CONTROL, Keycode.C)
        if(key.number == 4):
            if myPlatform == "mac":
                keyboard.send(Keycode.GUI, Keycode.X)
            else:
                keyboard.send(Keycode.LEFT_CONTROL, Keycode.X)
        if(key.number == 8):
            if myPlatform == "mac":
                keyboard.send(Keycode.GUI, Keycode.V)
            else:
                keyboard.send(Keycode.LEFT_CONTROL, Keycode.V)


        if(key.number == 2):
            if myPlatform == "mac":
                keyboard.send(Keycode.GUI, Keycode.Z)
            else:
                keyboard.send(Keycode.LEFT_CONTROL, Keycode.Z)
        if(key.number == 6):
            if myPlatform == "mac":
                keyboard.send(Keycode.GUI, Keycode.LEFT_SHIFT, Keycode.Z)
            else:
                keyboard.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.Z)

        if(key.number == 10):
            if myPlatform == "mac":
                keyboard.send(Keycode.GUI, Keycode.F)
            else:
                keyboard.send(Keycode.LEFT_CONTROL, Keycode.F)

        if(key.number == 9):
            if myPlatform == "mac":
                keyboard.send(Keycode.GUI, Keycode.S)
            else:
                keyboard.send(Keycode.LEFT_CONTROL, Keycode.S)


        if(key.number == 1):
            if myPlatform == "mac":
                keyboard.send(Keycode.GUI, Keycode.A)
            else:
                keyboard.send(Keycode.LEFT_CONTROL, Keycode.A)
        if(key.number == 5):             # assumes home/end are mapped like PC
                keyboard.send(Keycode.HOME)
                keyboard.send(Keycode.LEFT_SHIFT, Keycode.END)





        if(key.number == 3):
            mySendString('<pre class="nice-pre4"><code>')
        if(key.number == 7):
            mySendString('</code></pre>')

        if(key.number == 11):
            mySendString('&lt;')
        if(key.number == 15):
            mySendString('&gt;')

        if(key.number == 13):
            mySendString('xxxxxx')
        if(key.number == 14):
            mySendString('xxxxx')

        #if(key.number == 15):
        #    key.set_led(*(255,0,0))
        #    key.led_on()
        #    if myPlatform == "mac":
        #    myPlatform = "pc"
        #    if myPlatform == "pc":
        #        myPlatform = "mac"



    # A release handler that turns off the LED
    @keybow.on_release(key)
    def release_handler(key):
        key.led_off()

while True:
    # Always remember to call keybow.update()!
    keybow.update()
