# jlapse
jlapse can take screenshot and also take screenshot at an interval.Good for taking screenshot for timelapse video.
All the commands are by default optional.

# Available commands:
1.-s (start frame number,default is 1)
  2.-n (number of frames, or number of screen shot to take,default is 1)
  3.-d (delay time,minimum delay time is 1 second,default is 1)
  4.-p (name prefix, will be used as the image name,eg, if name prefix is screen_, then the image name will be like screen_23.png,
        default is screenshot_)
  5.-e (image extension,valid values are png,gif,jpg,default is png)
  6.-r (resolution of the image default is 1280x720)
  7.-o (output directory,a path to where the images will be saved,default to the current directory where the main.py is)
  8.-h (display help)

# How to use it?
1.python main.py  (will take one screen shot, when not a single argument is passed.)
2.python main.py -h (will show the help.)
3.python main.py -s 1 -n 5 -d 2 (will take 5 screenshots at an interval of 2 second.)
4.python main.py -n 10 (will take 10 screenshots at an interval of 1 second.)
5.python main.py -p my_shots_ (will take one screenshot and save that image with a name my_shots_1.png.)
6.python main.py -r 1024x768 (will take one screenshot and the image size will be the size of 1024x768.)
7.python main.py -n 10 -o shots_directory (will take 10 screenshots and save them to a directory named shots_directory.)
