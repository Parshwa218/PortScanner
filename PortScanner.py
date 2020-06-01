import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

print("********* Coded By Parshwa Bhavsar********")


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter the IP you want to scan: ")
port = int(input("Enter the Port you want to scan: "))


def portScanner(port):
	if s.connect_ex((host,port)):
		print("The port is closed")
	else:
		print("The port is open")

portScanner(port)


print("********************  Thank You ************************")
