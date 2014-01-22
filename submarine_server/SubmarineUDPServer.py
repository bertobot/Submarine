
from UDPServer import UDPServer
from SubmarineMovement import SubmarineMovement

class SubmarineUDPServer:
	def __init__(self, port):
		self.submarine = SubmarineMovement()
		self.udpServer = UDPServer(port, self.ourCallback)

	def ourCallback(data, addr):
		print "received: ", data
		whitespace = "\\s"
		self.submarine.move(data.split(whitespace))

	def start(self):
		self.udpServer.start()

