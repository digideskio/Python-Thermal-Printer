import itertools
import json
import re
import urllib2
import time
from Adafruit_Thermal import *

today = time.strftime("%Y-%m-%d")
text = urllib2.urlopen('http://dcsd.nutrislice.com/menu/meadow-view/lunch/').read()
menus = json.loads(re.search(r"bootstrapData\['menuMonthWeeks'\]\s*=\s*(.*);", text).group(1))

try:

	days = itertools.chain.from_iterable(menu['days'] for menu in menus)
	day = next(itertools.dropwhile(lambda day: day['date'] != '2014-01-13', days), 1)

	printer.inverseOn()
	printer.printlf('{:^32}'.format("Lunch for " + today))
	printer.inverseOff()

	printer.printlf('\n'.join(item['food']['name'] for item in day['menu_items']))

except:

	print "No lunch today at school."
