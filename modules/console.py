#!/usr/bin/env python3

import display
import sys

class Console(display.Display):
	def PrintString(self, string):
		sys.stdout.write(string)


if __name__ == "__main__":
	console = Console()
	console.PrintString("test message1")
	console.PrintString("test message2")


