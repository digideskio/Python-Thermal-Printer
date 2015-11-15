from __future__ import print_function
import urllib, time, json, requests
from Adafruit_Thermal import *
from xml.dom.minidom import parseString

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

text = urllib2.urlopen('http://rpprinter.azurewebsites.net/api/message').read()

messages = json.load(text)

for message in messages:
	print message.Text

#printer.print("testing 123")

#printer.feed(3)

#print("complete")