#!/usr/bin/env python3
import sys
import configparser
import os

class Application:
	def __init__(self,cfg_file):
		self._config = configparser.ConfigParser()
		self._config.read_file(open(cfg_file))

		#change sys.path to include location of custom modules
		module_path = os.getcwd()+"/modules"
		driver_path = module_path +"/drivers"
		sys.path.append(module_path)
		sys.path.append(driver_path)
		print(sys.path)
		#import modules
		import display
		import console 
		self._display_controller = display.DisplayController(console.Console())
		self._display_controller.DisplayStartupMessage()


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

