from submarine_app import app
from flask import render_template, redirect, request, current_app, session, flash, url_for
import time
import sys
import re
from Adafruit_PWM_Servo_Driver import PWM

import argparse
parser = argparse.ArgumentParser()
parser.parse_args()


# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 400  # Min pulse length out of 4096
servoMax = 440  # Max pulse length out of 4096
servoReverse = 440

vertical_pin = 0
left_pin = 1
right_pin = 2


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




@app.route('/', methods=["GET","POST"])
def index(function=None):
    error = []
    return render_template('index.html', error=error)

@app.route('/up')
def up():
    error = []
    print "up was processed."
    pwm.setPWM(vertical_pin, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(vertical_pin, 0, servoMin)
    return render_template('index.html', error=error)

@app.route('/down')
def down():
    error = []
    print "down was processed"
    return render_template('index.html', error=error)

@app.route('/left')
def left():
    error = []
    print "left was processed"
    pwm.setPWM(left_pin, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(left_pin, 0, servoMin)
    return render_template('index.html', error=error)

@app.route('/right')
def right():
    error = []
    print "right was processed"
    pwm.setPWM(right_pin, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(right_pin, 0, servoMin)
    return render_template('index.html', error=error)

@app.route('/stop')
def stop():
    error = []
    print "stop was processed"
    pwm.setPWM(right_pin, 0, servoMin)
    pwm.setPWM(left_pin, 0, servoMin)
    return render_template('index.html', error=error)

@app.route('/forward')
def forward():
    error = []
    print "forward was processed"
    pwm.setPWM(right_pin, 0, servoMax)
    pwm.setPWM(left_pin, 0, servoMax)
    return render_template('index.html', error=error)

