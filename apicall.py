from __future__ import print_function
import urllib, time, json, urllib2, re, os
import pygame, sys
from datetime import datetime
from dateutil import tz
import dateutil.parser
from Adafruit_Thermal import *
from xml.dom.minidom import parseString

from pygame.locals import *
import pygame.camera

width = 1920
height = 1080

#initialise pygame   
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(width,height))
cam.start()

#setup window
#windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
#pygame.display.set_caption('Camera')

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

	#take a picture
	image = cam.get_image()
	cam.stop()

	#display the picture
	#catSurfaceObj = image
	#windowSurfaceObj.blit(catSurfaceObj,(0,0))
	#pygame.display.update()

	pygame.image.save(windowSurfaceObj,'image.jpg')


#printer.print("testing 123")

#printer.feed(3)

#print("complete")