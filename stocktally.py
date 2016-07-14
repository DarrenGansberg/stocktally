#!/usr/bin/env python3
import configparser

class Application:
	def __init__(self,cfg_file):
		self._config = configparser.ConfigParser()
		self._config.read_file(open(cfg_file))

	def run():
		while(True):
			pass

	def shutdown():
		pass
			

def main():
	try:
		app = Application("config.cfg")
	except FileNotFoundError:
		print("\nconfig.cfg not found\n")
		print("Verify that config.cfg exists, before retrying\n")
	except KeyboardInterrupt:
		app.shutdown()

if __name__=="__main__": main()

