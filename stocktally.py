#!/usr/bin/env python3
import sys
import os

sys.path.append(os.getcwd()+"/modules")

from application import Application as Application
import console

class Stocktally(Application):
	def __init__(self):
		self._version = 0.01
		self._display = console.Console()

	def DisplayStartupMessage(self):
		self._display.PrintString("Stocktally v"+str(self._version)+"\n")

	def DisplayMainMenu(self):
		self._display.PrintString("Stocktally main menu: \n")
		self._display.PrintString("1. Update stock counts \n")
		self._display.PrintString("2. Exit program \n")
		self._display.PrintString("Enter Selection: \n")


def main():
	try:
		app = Stocktally()
		app.DisplayStartupMessage()
		app.DisplayMainMenu()

	#except FileNotFoundError:
	#	print("\nconfig.cfg not found\n")
	#	print("Verify that config.cfg exists, before retrying\n")

	except KeyboardInterrupt:
		app.Shutdown()

if __name__ == "__main__": main()
