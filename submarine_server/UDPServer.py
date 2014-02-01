
from socket import *

class UDPServer:
	def __init__(self, port, callback):
		self.port = port
		self.callback = callback
		self.address = "0.0.0.0"
		self.sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
		self.sock.bind((self.address, self.port))

	def onMessageReceived(self, callback):
		data, addr = self.sock.recvfrom(1024)
		self.callback(data, addr)

	def start(self):
		while True:
			self.onMessageReceived(self.callback);
		
