#!/usr/bin/env python3

class Display(object):
	def __init__(self):
		pass

	def PrintString(self, string):
		raise DisplayError("PrintString not implemented") 

class DisplayError(Exception):
	def __init__(self, message):
		self.message = message

if __name__ == "__main__": 
	import unittest

	class DisplayTests(unittest.TestCase):
		def test_PrintString_ThrowsDisplayError(self):
			with self.assertRaises(DisplayError):
				display = Display()
				display.PrintString("unit test")

	unittest.main()

