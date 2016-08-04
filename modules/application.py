#!/usr/bin/env python3
import messaging
import Queue

class Application(object):
	def __init__(self):
		self._message_queue = Queue.Queue()

	def GetMessage(self):
		return self._message_queue.get(True)

	def PostMessage(self, msg):
		self._message_queue.put(msg)

	def ProcessMessage(self, msg):
		raise ApplicationException("ProcessMessage not implemented")
 
	def Run(self):
		#blocks until a message is available. When a message is available
		#GetMessage() returns, quit on MSG_QUIT otherwise process message.
		while True:
			msg = self.GetMessage()
			if msg.GetId() == messaging.MSG_QUIT:
				break
			else:
				self.ProcessMessage(msg)
		return 0

	def Shutdown(self):
		raise ApplicationException("Shutdown not implemented")

class ApplicationException(Exception):
		def __init__(self, message):
			super(ApplicationException, self)

if __name__ == '__main__': 
	import unittest

	class ApplicationTests(unittest.TestCase):
		def test_Shutdown_ThrowsException(self):
			with self.assertRaises(ApplicationException):
				app = Application()
				app.Shutdown()

		def test_ProcessMessage_ThrowsException(self):
			with self.assertRaises(ApplicationException):
				app = Application()
				app.ProcessMessage(None)

		def test_Run_WhenReceivesMSG_QUIT_Returns0(self):
			expected_result = 0

			app = Application()
			app.PostMessage(messaging.Message(messaging.MSG_QUIT))
			actual_result = app.Run()

			self.assertEqual(expected_result,actual_result) 

	unittest.main()
