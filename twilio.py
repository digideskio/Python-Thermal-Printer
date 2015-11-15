from __future__ import print_function
import urllib, time
from Adafruit_Thermal import *
from xml.dom.minidom import parseString

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

printer.print("I love you Hayley!")

printer.feed(3)
printer.feed(3)

print("complete")