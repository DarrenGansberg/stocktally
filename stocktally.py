#!/usr/bin/env python3
import configparser

class Application:
	def __init__(self,cfg_file):
		self._config = configparser.ConfigParser()
		self._config.read_file(open(cfg_file))

	def Run(self):
		while(True):
			pass

	def Shutdown(self):
		print("\nClosing Stocktally")
			

def main():
	try:
		app = Application("config.cfg")
		app.Run()
	except FileNotFoundError:
		print("\nconfig.cfg not found\n")
		print("Verify that config.cfg exists, before retrying\n")
	except KeyboardInterrupt:
		app.Shutdown()

if __name__=="__main__": main()

