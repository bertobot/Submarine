
from UDPServer import UDPServer
from SubmarineMovement import SubmarineMovement

class SubmarineUDPServer:
	def __init__(self, port):
		self.submarine = SubmarineMovement()
		self.udpServer = UDPServer(port, self.ourCallback)
		self.toss = False;

	def ourCallback(data, addr):
		if (self.toss):
			self.toss = False
			return

		print "received: ", data

		whitespace = "\\s"
		self.submarine.move(data.split(whitespace))

		values = data.split(whitespace)

		if (values[0] == values[1] and values[1] == values[2] and values[2] == 0):
			self.toss = True

		self.submarine.move(values)

		

	def start(self):
		self.udpServer.start()

