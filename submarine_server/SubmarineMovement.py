import time
from Adafruit_PWM_Servo_Driver import PWM



# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)

class SubmarineMovement:
	def __init__(self):
		self.pwm = PWM(0x40, debug=True)
		self.servoMin = 400
		self.servoMax = 600
		self.servoReverse = 440
		self.vertical_pin = 0
		self.left_pin = 1
		self.right_pin = 2

	def setServoPulse(self, channel, pulse):
		self.pulseLength = 1000000                   # 1,000,000 us per second
		self.pulseLength /= 60                       # 60 Hz
		print "%d us per period" % self.pulseLength
		self.pulseLength /= 4096                     # 12 bits of resolution
		print "%d us per bit" % self.pulseLength
		self.pulse *= 1000
		self.pulse /= self.pulseLength
		self.pwm.setPWM(channel, 0, pulse)
		self.pwm.setPWMFreq(60)                        # Set frequency to 60 Hz


	def stop(self):
		self.pwm.setPWM(right_pin, 0, servoMin)
		self.pwm.setPWM(left_pin, 0, servoMin)
		self.pwm.setPWM(vertical_pin, 0, servoMin)

	def forward(self, vector):
		self.pwm.setPWM(left_pin, vector, servoMax)
		self.pwm.setPWM(right_pin, vector, servoMax)

	def turn(self, vector):
		if (vector >= 0):
			self.pwm.setPWM(left_pin, vector, servoMax)
		else:
			self.pwm.setPWM(right_pin, vector, servoMax)
		

	def move(self, xx, yy, zz):
		self.turn(xx)
		self.forward(yy);

		self.pwm.setPWM(vertical_pin, topMotor, servoMax)
	
