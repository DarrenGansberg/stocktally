#!/usr/bin/env python3

class DisplayController:
	def DisplayStartupMessage(self):
		print("Display Startup Message")
	def DisplayShutdownMessage(self):
		print("Display Shutdown Message")

#Creates a Display Controller
def CreateDisplayController():
	return DisplayController()
