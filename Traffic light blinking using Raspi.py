
#Traffic light blinking using Raspi

import Rpi.GPIO as GPIO
import time
GPIO.setwarnings(False)

#set up variable
green=11
yellow=10
red=9

#set up the numbering scheme
GPIO.setmode(GPIO.BCM)

#set the mode on the pins to out
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)

#initially turn the lights off
GPIO.output(green,False)
GPIO.output(yellow,False)
GPIO.output(red,False)

#turn green on for 3sec
GPIO.output(green,False)
time.sleep(3)

#turn yellow on for 3 sec
GPIO.output(green,False)
GPIO.output(yellow,False)
time.sleep(3)

#turn red on for 3sec
GPIO.output(yellow,False)
GPIO.output(red,False)
time.sleep(10)




