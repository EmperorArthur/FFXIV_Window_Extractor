#!/usr/bin/env python3
# Program to extract turnins from a FFXIV screenshot
import re
import subprocess
import argparse


#Return the X and Y location of the close button in the image
def get_X_location(in_image, stop_at_first_match = True):
    compare_args   = ['compare', '-metric', 'RMSE', '-similarity-threshold', str(int(not(stop_at_first_match))), '-subimage-search', in_image, 'Win_Close.png', 'temp_out.png']
    raw_location = subprocess.run(compare_args,stderr=subprocess.PIPE).stderr
    m = re.search('.*@\ ([0-9]*),([0-9]*)', str(raw_location))
    return (int(m.group(1)),int(m.group(2)))

def crop_window(in_image,out_image,window_size,X_button_location):
    #Calculate the image's relative location from the close button position
    window_x = window_size[0]
    window_y = window_size[1]
    #These are the offset's of the 'X' button from the top,right of the image
    x_offset = 28
    y_offset = 7
    start_x = str(location[0]-window_x+x_offset)
    start_y = str(location[1]-y_offset)
    location_str = '{window_x}x{window_y}+{start_x}+{start_y}'.format(**locals())
    crop_args      = ['convert', '-crop', location_str, in_image, out_image]
    subprocess.run(crop_args)

parser = argparse.ArgumentParser(description='Extract a window from FFXIV.')
parser.add_argument('in_file', type=str, help='The input screenshot with a window open.')
parser.add_argument('-o','--output', type=str, help='Output the window to this file.',default='Turnins_window.png')
args = parser.parse_args()

location = get_X_location(args.in_file)
print("Found Window 'X' Button at: ",location)
crop_window(args.in_file,args.output,(723,511),location)
