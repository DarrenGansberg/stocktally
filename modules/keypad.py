#!/usr/bin/env python3

import threading
import messaging

class Keypad(object):
	def __init__(self, callback):
		if callback is None:
			raise Exception("callback cannot be None")
		self._callback = callback
		self._thread = threading.Thread(None, self._Read)
		self._thread.daemon = True

	def _Read(self):
		pass

	def Start(self):
		self._thread.start()


