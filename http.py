#coding: utf-8

import sys
import socket
import argparse
import requests

class testReq:
	def test(self,url):
		self.r = requests.get(url,verify=True)
		print self.r.status_code

if __name__ == '__main__':
	desc = 'host for the request'
	parser = argparse.ArgumentParser(description= desc)
	parser.add_argument("-u","--url",type = str,required=True)
	options = parser.parse_args()
	req = testReq()
	req.test(options.url)




