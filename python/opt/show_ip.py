# コンテナのIPを調べる

from ipaddress import ip_address
import socket

if __name__ == "__main__":
	host_name = socket.gethostname()
	ip_addr = socket.gethostbyname(host_name)
	print(host_name)
	print(ip_addr)
