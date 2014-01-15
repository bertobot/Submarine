from UDPServer import UDPServer

def mycallback(data, addr):
	print "received: ", data


server = UDPServer(5500, mycallback)

server.start()
