import bluetooth
import json

def client():
	
	sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

	bt_addr=input("addr bl: ")
	port = 0x1001

	print("trying to connect to %s on PSM 0x%X" % (bt_addr, port))

	sock.connect((bt_addr, port))

	print("connected.  type stuff")
	sock.send(json.dumps({"ssid": input("ssid: "), "passwd": input("passwd: ")}))
	data = json.loads(sock.recv(1024))
	print("Data received:", str(data))

	sock.close()


def main():
	client()
	

if __name__ == "__main__":
	main()
