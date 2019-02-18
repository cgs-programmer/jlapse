# -*- coding: utf-8 -*-
import unittest
from mock import patch
import main

# lets do some testing and some faking
class Test_HandleCommandLineArguments_0(unittest.TestCase):
	def setUp(self):
		self.command_handle = main.HandleCommandLineArguments()
		# mock the return value of the response
		self.command_handle.response = [True,{'-s': 1,'-n': 5,'-d': 1}]

	# mock the parse_arguments function
	@patch('main.HandleCommandLineArguments.parse_arguments')
	def test_parse_arguments(self,mock_obj):
		mock_obj.return_value = [True,{'-s': 1,'-n': 5,'-d': 1}]
		expected = [True,{'-s': 1,'-n': 5,'-d': 1}]
		self.assertEqual(self.command_handle.parse_arguments(),expected)

	# mock the get_response_obj
	@patch('main.HandleCommandLineArguments.get_response_obj')
	def test_get_response_obj(self,mock_obj):
		mock_obj.return_value = [True,{'-s': 1,'-n': 5,'-d': 1}]
		expected = [True,{'-s': 1,'-n': 5,'-d': 1}]
		self.assertEqual(self.command_handle.get_response_obj(),expected)

	# test 3 arguments are passed
	def test_get_len_of_commands_list(self):
		expected = 3
		self.assertEqual(self.command_handle.get_len_of_commands_list(),expected)

	# test the get_commands_list
	def test_get_commands_list(self):
		expected = '-s'
		self.assertEqual(next(self.command_handle.get_commands_list()),expected)

	def tearDown(self):
		del(self.command_handle)

class Test_HandleCommandLineArguments_01(unittest.TestCase):
	def setUp(self):
		self.command_handle = main.HandleCommandLineArguments()

	# test when not a single argument is passed
	def test_get_len_of_commands_list(self):
		expected = 0
		self.assertEqual(self.command_handle.get_len_of_commands_list(),expected)

	def tearDown(self):
		del(self.command_handle)

class Test_JLapse(unittest.TestCase):
	def setUp(self):
		pass

	# test JLapse class
	@patch('main.HandleCommandLineArguments.get_len_of_commands_list')
	@patch('main.HandleCommandLineArguments.get_response_obj')
	@patch('main.JLapse.takeScreenShots')
	def test_jlapse(self,mock_obj0,mock_obj1,mock_obj2):
		mock_obj0.return_value = True # takeScreenShots return value
		mock_obj1.return_value = [True,{'-s': 1,'-n': 2,'-d': 1}] # get_response_obj return value
		mock_obj2.return_value = 3 # get_len_of_commands_list return value
		jlapse = main.JLapse()

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()