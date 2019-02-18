# -*- coding: utf-8 -*-
import sys
import re

# command line argumets parser 
# created by Joseph Chhetri
# Date 02-02-2019
# all the command arguments are optional by default

class CommandLineParser(object):
	def __init__(self):
		self.accepted_arguments_list = []
		self.help_texts_list = []

	def __str__(self):
		return 'CommandLineParser object'

	def __repr__(self):
		return 'CommandLineParser object'

	# format the commands into a parseable list
	# only standard charcters are allowed
	# whitespaces not allowed
	# - is also not allowed
	def formatCommands(self):
		if (not len(sys.argv) > 1):
			return False
		sys.argv.append(' ')
		command_string = ' '.join(sys.argv[1:])
		formated_commands = []
		pattern = re.compile(r'-[a-zA-Z]+ [^\s-]*')
		matches = pattern.finditer(command_string)
		for i in matches:
			formated_commands.append(i.group(0).rstrip())
		for i in range(len(formated_commands)):
			if (not ' ' in formated_commands[i]):
				formated_commands[i] += ' 0'

		return formated_commands

	# call this function after adding the arguments
	def parseArguments(self):
		formated_commands = self.formatCommands()
		if (not formated_commands):
			return False
		for args in formated_commands:
			if (not args.split(' ')[0] in self.accepted_arguments_list):
				return False
		arguments_list = []
		for i in formated_commands:
			arguments_list.append(i.split(' '))
		self.arguments_dict = dict(arguments_list)
		return True,self.arguments_dict

	# add arguments for the command line
	def addArgument(self,short_name,help_text = ''):
		self.accepted_arguments_list.append(short_name)
		self.help_texts_list.append(help_text)
		return short_name

	# get the arguments dict dictionary
	def get_argumentsDict(self):
		return self.arguments_dict

	# get the arguments help texts list
	def get_helpTexts(self):
		if (not len(self.help_texts_list) > 1):
			return False
		return self.help_texts_list

	# get the arguments keys
	def get_argsKeys(self):
		keys = []
		for argsk in self.arguments_dict.iterkeys():
			keys.append(argsk)
		# returns sorted list
		return keys

	# get the arguments values
	def get_argsValues(self):
		values = []
		for argsv in self.arguments_dict.itervalues():
			values.append(argsv)
		return values

	# display Help
	def showHelp(self):
		print ("COMMANDS:-")
		print("*"*50)
		for help_item_number in xrange(0,len(self.accepted_arguments_list)):
			print ("\t{0}     {1}".format(self.accepted_arguments_list[help_item_number],
					self.help_texts_list[help_item_number]))
		print ("*"*50)
		print ("Created by Joseph Chhetri. Date 02/02/2019")

	def __del__(self):
		return True
