import socket
import sys
import os

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner):
	f = open('vuln_banners.txt', 'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print '[+] Server is vulnerable: ' + banner.strip('\n')

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print '[-] ' + filename + ' does not exist.'
			exit(0)
		if not os.access(filename, os.R_OK):
			print '[-] ' + filename + ' access denied.'
			exit(0)
		print '[+] Reading Vulnerabilities From: ' +  filename
	else:
		print '[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>'
		exit(0)
		portList = [21,22,25,80,110,443]
		for x in range(1, 255):
			ip = '192.168.95.' + str(x)
			for port in portList:
				banner = retBanner(ip, port)
				if banner:
					print '[+] ' + ip + ': ' + banner
					checkVulns(banner)

if __name__ == '__main__':
	main()