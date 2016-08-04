#!/usr/bin/env python3
import sys
import os

sys.path.append(os.getcwd()+"/modules")

from application import Application as Application
import console
import keyboard

class Stocktally(Application):
	def __init__(self):
		super(Stocktally,self).__init__()
		self._version = 0.01
		self._display = console.Console()
		self._input = keyboard.Keyboard(self.PostMessage)

	def _DisplayStartupMessage(self):
		self._display.PrintString("Stocktally v"+str(self._version)+"\n")

	def _DisplayMainMenu(self):
		self._display.PrintString("Stocktally main menu: \n")
		self._display.PrintString("1. Update stock counts. \n")
		self._display.PrintString("2. Exit program. \n")
		self._display.PrintString("Enter Selection: ")

	def _DisplayShutdownMessage(self):
		self._display.PrintString("\nThank you for using Stocktally\n")

	def ProcessMessage(self, msg):
		self._display.PrintString(str(msg.GetId()))


	def Run(self):
		self._DisplayStartupMessage()
		self._DisplayMainMenu()
		self._input.Start()
		return super(Stocktally,self).Run()

	def Shutdown(self):
		self._DisplayShutdownMessage()

def main():
	try:
		app = Stocktally()

		if app.Run():
			#could report error to user here
			pass
		else:
			app.Shutdown()
	#except FileNotFoundError:
	#	print("\nconfig.cfg not found\n")
	#	print("Verify that config.cfg exists, before retrying\n")

	except KeyboardInterrupt:
		app.Shutdown()

if __name__ == "__main__": main()
