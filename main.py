# -*- coding: utf-8 -*-
# jlapse version 0.2
# date 16-february-2019
# a simple screenshot tool and timelapse creator tool
import time
import ctypes
import sys
from PIL import ImageGrab,Image
from c_parse.c_parse import CommandLineParser

# handles the command line arguments
class HandleCommandLineArguments(object):
	def __init__(self):
		self.commands_list = []
		self.commands = CommandLineParser()
		self.add_arguments()
		self.response = self.parse_arguments()

	# string reprsentation of a class
	def __str__(self):
		return 'HandleCommandLineArguments object'

	# representation of the class
	def __repr__(self):
		return 'HandleCommandLineArguments object'

	# add acceptable arguments
	def add_arguments(self):
		start_frame = self.commands.addArgument('-s',help_text = "start frame number.")
		number_of_frames = self.commands.addArgument('-n',help_text = "number of frames to capture.")
		delay_time = self.commands.addArgument('-d',help_text = "delay time.")
		name_prefix = self.commands.addArgument('-p',help_text = "name prefix.")
		extension = self.commands.addArgument('-e',help_text = "extension.")
		resolution = self.commands.addArgument('-r',help_text = "resolution.")
		output_directory = self.commands.addArgument('-o',help_text = "output directory.")
		help_ = self.commands.addArgument('-h',help_text = "show help.")
		self.commands_list.append(start_frame)
		self.commands_list.append(number_of_frames)
		self.commands_list.append(delay_time)
		self.commands_list.append(name_prefix)
		self.commands_list.append(extension)
		self.commands_list.append(resolution)
		self.commands_list.append(output_directory)
		self.commands_list.append(help_)

	# parse the arguments
	def parse_arguments(self):
		response = self.commands.parseArguments()
		return response

	# get the len of commands passed
	def get_len_of_commands_list(self):
		try:
			return len(self.response[1])
		except:
			return 0

	# get the response object
	def get_response_obj(self):
		return self.response

	# get the acceptable commands list
	def get_commands_list(self):
		for i in self.commands_list:
			yield i

	# display the help
	def display_help(self):
		print ("usage: python main.py -s [] -n [] -d [] -p [] -e [] -r [] -o []")
		print ("Example: python main.py -s 1 -n 1 -d 1 -p screenshot_ -e png -r 1024x768 -o shots")
		self.commands.showHelp()

	# delete this object
	def __del__(self):
		return True

class JLapse(object):
	"""
	This class is responsible for taking screen shots.
	"""
	def __init__(self):
		# -------------------------------------------------
		try:
			user32 = ctypes.windll.user32
			screenWidth,screenHeight = user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)
		except:
			screenWidth,screenHeight = 1280,720
		self.command_handle = HandleCommandLineArguments()
		commands_list = self.command_handle.get_commands_list()
		len_of_commands_list = self.command_handle.get_len_of_commands_list()
		response = self.command_handle.get_response_obj()
		# -------------------------------------------------
		# default arguments
		self.start_frame = 1
		self.number_of_frames = 1
		self.delay_time = 1
		self.name_prefix = 'screenshot_'
		self.extension = 'png'
		self.size = '{0}x{1}'.format(screenWidth,screenHeight)
		self.output_directory = '.'
		self.help_ = False
		# -------------------------------------------------
		self.check_arguments(response,commands_list)
		# -------------------------------------------------
		if (len_of_commands_list == 1 and self.help_):
			self.command_handle.display_help()
		else:
			self.takeScreenShots(self.start_frame,self.number_of_frames,self.delay_time,self.name_prefix,self.extension,self.size,self.output_directory)

	def __str__(self):
		return 'JLapse object'

	def __repr__(self):
		return 'JLapse object'

	# check the arguments passed in and then update the default arguments
	def check_arguments(self,response_obj,commands_list_obj):
		if (not response_obj == False):
			# start frame
			t_start_frame = next(commands_list_obj)
			if (t_start_frame in response_obj[1]):
				self.start_frame = int(response_obj[1][t_start_frame])
			# number of frames
			t_number_of_frames = next(commands_list_obj)
			if (t_number_of_frames in response_obj[1]):
				self.number_of_frames = int(response_obj[1][t_number_of_frames])
			# delay time
			t_delay_time = next(commands_list_obj)
			if (t_delay_time in response_obj[1]):
				self.delay_time = int(response_obj[1][t_delay_time])
			# name prefix
			t_name_prefix = next(commands_list_obj)
			if (t_name_prefix in response_obj[1]):
				self.name_prefix = response_obj[1][t_name_prefix]
			# extension
			t_extension = next(commands_list_obj)
			if (t_extension in response_obj[1]):
				self.extension = response_obj[1][t_extension]
			# size
			t_size = next(commands_list_obj)
			if (t_size in response_obj[1]):
				self.size = response_obj[1][t_size]
			# output directory
			t_output_directory = next(commands_list_obj)
			if (t_output_directory in response_obj[1]):
				self.output_directory = response_obj[1][t_output_directory]
			# help
			if (next(commands_list_obj) in response_obj[1]):
				self.help_ = True

	# takes one screen shot if no argument is passed
	# can take sceen shots at an interval
	def takeScreenShots(self,startFrame,numOfFrames,delay,prefix,extension,size,output_dir):
		resolution = size.split("x")
		sizeX = int(resolution[0])
		sizeY = int(resolution[1])
		for screen in range(startFrame,numOfFrames+1):
			t1 = time.time()
			screenShot = ImageGrab.grab()
			image = screenShot.resize((sizeX,sizeY),Image.ANTIALIAS)
			image.save("{0}/{1}{2}.{3}".format(output_dir,prefix,screen,extension),"{0}".format(extension))
			sys.stdout.write("\r" + "Status: {0}/{1}".format(screen,numOfFrames))
			sys.stdout.flush()
			t2 = time.time()
			ptime = t2-t1
			wait_time = delay-ptime
			time.sleep(wait_time)
		return True

	# delete this object
	def __del__(self):
		return True


def main():
	jlapse = JLapse()

if __name__ == '__main__':
	main()




