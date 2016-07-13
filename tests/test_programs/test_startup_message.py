#!/usr/bin/env python3

import sys
sys.path.append("../../presentation/")
from console import Console as Console

def main():
	console = Console()
	console.DisplayStartupMessage()

if __name__ == "__main__": main()
