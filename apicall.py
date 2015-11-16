from __future__ import print_function
import urllib, time, json, urllib2, re
from datetime import datetime
from dateutil import tz
import dateutil.parser
from Adafruit_Thermal import *
from xml.dom.minidom import parseString
import subprocess
import azureblob

import datetime 
todays_date = datetime.datetime.today() 
image_name = todays_date.strftime('%m-%d-%y-%H%M') 

azureblob.upload("image2.jpg", image_name + '.jpg')

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

text = urllib2.urlopen('http://rpprinter.azurewebsites.net/api/unread').read()

messages = json.loads(text)

for message in messages:
	printer.print('--------------------------------')
	printer.print('From: ' + message["FromName"])
	printer.feed(1)

	from_zone = tz.gettz('UTC')
	to_zone = tz.gettz('US/Pacific')

	utc = dateutil.parser.parse(message["CreatedDateTime"])
	utc = utc.replace(tzinfo=from_zone)
	pacific = utc.astimezone(to_zone)

	printer.print('Date: ' + pacific.strftime('%x %X'))

	printer.feed(1)
	printer.print('Message:')
	printer.feed(2)
	printer.print(message["Text"])
	printer.feed(1)
	printer.print('--------------------------------')
	printer.feed(4)


	grab_cam = subprocess.Popen("sudo fswebcam -r 1920x1080 -d /dev/video0 -q /home/motion/%m-%d-%y-%H%M.jpg", shell=True) #replace as necessary
	grab_cam.wait()

	#print "Acquiring image file...." 
	import datetime 
	todays_date = datetime.datetime.today() 
	image_name = todays_date.strftime('%m-%d-%y-%H%M') 
	image_path = '/home/motion/' + image_name + '.jpg' 

	azureblob.upload(image_path, image_name + '.jpg')


#printer.print("testing 123")

#printer.feed(3)

#print("complete")