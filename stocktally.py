#!/usr/bin/env python3
import sys
import os

sys.path.append(os.getcwd()+"/modules")

from application import Stocktally as Application
from console import Console as Console


def main():
	try:
		app = Application("config.cfg")
		console = Console(app)
		console.DisplayStartupMessage()
		app.Run()
	except FileNotFoundError:
		print("\nconfig.cfg not found\n")
		print("Verify that config.cfg exists, before retrying\n")
	except KeyboardInterrupt:
		app.Shutdown()

if __name__ == "__main__": main()
