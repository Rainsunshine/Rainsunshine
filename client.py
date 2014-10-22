#coding: utf-8

import sys
import socket
import argparse

def parse_url(url):
	url_parts = url.split("://")
	scheme = url_parts[0]
	if scheme == 'https':
		print 'not support ssl'
		sys.exit(0)
	else:
		url_part2 = url_parts[1]
		path_location = url_part2.find('/',0,len(url_part2))
		if path_location != -1:
			host = url_part2[:path_location]
		else:
			host = url_part2
	return host

def send_request(url):
	host = parse_url(url)
	port = 80

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		s.connect((host,port))
	except:
		print 'can not connect'
	header = ('GET / HTTP/1.1\r\n'
		'Host:%s\r\nConnection:keep-alive\r\n'
		'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36\r\n'
		'/r/n') % host
	s.sendall(header)
	data = s.recv(4096)
	s.close()
	head = data.split('/r/n/r/n')[0]
	print(head)

if __name__ == '__main__':
	desc = 'host for the request'
	parser = argparse.ArgumentParser(description = desc)
	parser.add_argument("-u","--url",type=str,required=True)
	options = parser.parse_args()
	send_request(options.url)
