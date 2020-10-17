from wireless import Wireless
import bluetooth
import json

def runServer():
	server_sock=bluetooth.BluetoothSocket( bluetooth.L2CAP )

	port = 0x1001

	server_sock.bind(("",port))
	server_sock.listen(1)
        while True:
		client_sock,address = server_sock.accept()
		print("Accepted connection from ",address)

		data = setWifi(json.loads(client_sock.recv(1024)).values())
		print("Data received: ", str(data))
	
		client_sock.send(json.dumps(data))

		
		client_sock.close()
	server_sock.close()


def setWifi(sattg, interface="wlan0"):
	wire = Wireless(interface)
	return {"status": wire.connect(ssid=sattg[0], password=sattg[1])}


def main():
	runServer()

if __name__ == "__main__":
	main()
 
