#!/usr/bin/env python3

MSG_QUIT = 1
MSG_COMMAND = 2 
MSG_KEYPRESSED = 3

COMMAND_QUIT = 1


class Message(object):
	def __init__(self, id):
		self._id = id

	def GetId(self):
		return self._id

class KeyPressed(Message):
		def __init__(self, key):
			super(KeyPressed,self).__init__(MSG_KEYPRESSED)
			self._key = key

		def GetKey(self):
			return self._key


class Command(Message):
		def __init__(self, command):
			super(Message,self).__init__(MSG_COMMAND)
			self._command = command

		def GetCommand(self):
			return self._command
	
