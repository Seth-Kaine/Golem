#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
print(">>>>>>> importation passed! >>>>>>>>>")
# Needs to be BCM. GPIO.BOARD lets you address GPIO ports by periperal
# connector pin number, and the LED GPIO isn't on the connector
ledpin = 23


GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(ledpin, GPIO.OUT)

# Off
GPIO.output(ledpin, GPIO.LOW)

print(">>>>>>> GPIO GPIO23 OFF >>>>>>>>>")
# Wait a bit
sleep(1)

# On
GPIO.output(ledpin, GPIO.HIGH)
print(">>>>>>> GPIO GPIO23 ON >>>>>>>>>")

# Off
sleep(2)
GPIO.output(ledpin, GPIO.LOW)

print(">>>>>>> GPIO GPIO23 OFF >>>>>>>>>")
# Wait a bit
sleep(1)

# On
GPIO.output(ledpin, GPIO.HIGH)
print(">>>>>>> GPIO GPIO23 ON >>>>>>>>>")