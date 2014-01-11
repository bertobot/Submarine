#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys
import re

import argparse
parser = argparse.ArgumentParser()
parser.parse_args()


# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 165  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoReverse = 300

vertical_servo_pin = 0
left_servo_pin = 1
right_servo_pint = 2

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

def up(vertical_servo_pin):
    
    while (True):
        print "Going Up"
        pwm.setPWM(vertical_servo_pin, 0, servoMax)

def down(vertical_servo_pin):
    while (True):
        print "Diving"
        pwm.setPWM(vertical_servo_pin, 0, servoReverse)

def left(left_servo_pin):
    while (True):
        print "Turning Left"
        pwm.setPWM(left_servo_pin, 0, servoMax)

def right(right_servo_pin):
    while (True):
        print "Turning Right"
        pwm.setPWM(right_servo_pin, 0, servoMax)

def back(right_servo_pin,left_servo_pin):
    while (True):
        print "Reverse"
        pwm.setPWM(right_servo_pin, 0, servoReverse)
        pwm.setPWM(left_servo_pin, 0, servoReverse)


def usage():
    """Motor controller Usage: """

    

def main():
    for line in fileinput.input():
        pass

        
if __name__ == "__main__":
    main()

