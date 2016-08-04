#!/usr/bin/env python3
import threading
import messaging

class Keyboard:
	def __init__(self, callback):
		self._callback = callback
		self._thread = threading.Thread(None, self._Read)
		self._thread.daemon = True 
		self._getch = _Getch()

	def _Read(self):
		while True:
			c = self._getch()
			if c == "\x03":
				self._callback(messaging.Command(messaging.COMMAND_QUIT))
				break
			else:
				msg = messaging.KeyPressed(self._getch())
				self._callback(msg)

	def Start(self):
		self._thread.start()

#http://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user/510364#510364

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

