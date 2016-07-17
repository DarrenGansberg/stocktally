#!/usr/bin/env python3

class Console:
	def __init__(self, app):
		self._app = app

	def DisplayStartupMessage(self):
		print(self._app.GetStartupMessage())

	def DisplayShutdownMessage(self):
		print(self._app.GetShutdownMessage())
