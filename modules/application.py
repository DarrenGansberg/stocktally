#!/usr/bin/env python3
import sys
import configparser
import os

class Stocktally:
	def __init__(self,cfg_file):
		self._config_file = cfg_file
		self._version = 0.01
		self._startup_message = "Starting Stocktally version {}".format(self._version)
		self._shutdown_message = "Closing Stocktally"

	def GetStartupMessage(self):
		return self._startup_message

	def GetShutdownMessage(self):
		return self._shutdown_message

	def Run(self):
		while(True):
			pass
	def Shutdown(self):
		print("\nClosing Stocktally")
