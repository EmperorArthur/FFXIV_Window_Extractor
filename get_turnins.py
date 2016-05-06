#!/usr/bin/env python3
# Program to extract turnins from a FFXIV screenshot
import re
import subprocess

screenshot     = 'Turnins 5-5-2016.png'
compare_args   = ['compare', '-metric', 'RMSE', '-similarity-threshold', '0.0', '-subimage-search', screenshot, 'Win_Close.png', 'temp_out.png']

raw_location = subprocess.run(compare_args,stderr=subprocess.PIPE).stderr
m = re.search('.*@\ ([0-9]*),([0-9]*)', str(raw_location))
location = (int(m.group(1)),int(m.group(2)))

crop_args      = ['convert', '-crop', '725x515+'+str(location[0]-695)+'+'+str(location[1]-10), screenshot, 'Turnins_window.png']

subprocess.run(crop_args)
