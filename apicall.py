from __future__ import print_function
import urllib, time, json, urllib2, re
from Adafruit_Thermal import *
from xml.dom.minidom import parseString

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

text = urllib2.urlopen('http://rpprinter.azurewebsites.net/api/unread').read()

messages = json.loads(text)

for message in messages:
	printer.print('From: ' + message["FromName"])
	printer.feed(1)
	printer.print('Date: ' + message["CreatedDateTime"].strftime("%B %d, %Y"))
	printer.feed(1)
	printer.print('Message:')
	printer.feed(2)
	printer.print(message["Text"])
	printer.feed(3)

#printer.print("testing 123")

#printer.feed(3)

#print("complete")