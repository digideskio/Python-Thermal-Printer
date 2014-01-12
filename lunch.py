#from __future__ import print_function
from Adafruit_Thermal import *
import itertools
import json
import re
import urllib2
import time

today = time.strftime("%Y-%m-%d")

printer.print(today)

text = urllib2.urlopen('http://dcsd.nutrislice.com/menu/meadow-view/lunch/').read()
menus = json.loads(re.search(r"bootstrapData\['menuMonthWeeks'\]\s*=\s*(.*);", text).group(1))

days = itertools.chain.from_iterable(menu['days'] for menu in menus)

day = next(itertools.dropwhile(lambda day: day['date'] != '2014-01-13', days), None)

if day:
    print '\n'.join(item['food']['name'] for item in day['menu_items'])
else:
    print 'Day not found.'
