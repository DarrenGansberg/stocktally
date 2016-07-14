#!/usr/bin/env python3
import configparser

class Application:
	def __init__(self,cfg_file):
		self._config = configParser()
		self._config.read_file(open(cfg_file))

	def run():
		while(True):
			pass

	def shutdown():
		pass
			

def main():
	try:
		app = Application("config.cfg")
	except KeyboardInterrupt:
		app.shutdown()

if __name__=="__main__": main()

