#!/usr/bin/env python
# coding: utf-8

# You need PIL <http://www.pythonware.com/products/pil/> to run this script
# Download unifont.ttf from <http://unifoundry.com/unifont.html> (or use
# any TTF you have)
# Copyright 2020 @luk0y
# License: GPL <http://www.gnu.org/copyleft/gpl.html>

from image_utils import ImageText

import time
import os

os.environ['TZ'] = 'Asia/Kolkata'

time.tzset()

font, font_2, font_3  = 'fonts/arial.ttf','fonts/Moon_Bold.otf','fonts/Alcubierre.otf'
 
color = (50, 50, 50)

def quoteGen(data):

	text = data['QUOTE']

	author = data['AUTHOR']
	a = time.strftime('%r\n%d/%m/%Y')

	img = ImageText("bg-images/rsz_photo-1517816743773-6e0fd518b4a6.jpg", background=(255, 255, 255, 200))
	
	#You don't need to specify text size: can specify max_width or max_height
	# and tell write_text to fill the text in this space, so it'll compute font
	# size automatically
	#write_text will return (width, height) of the wrote text

	img.write_text((525, 600), a, font_filename=font_3,
	               font_size=20, max_height=150, color=color)
	               

	if len(text) >= 130 and len(text) <= 250:
		img.write_text_box((100, 200), text, box_width=400, font_filename=font,
			font_size=25, color=color, place='center')

		img.write_text((300, 500), 'Author : '+author, font_filename=font,
	               font_size=19, max_height=150, color=color)

		img.save('sample-imagetext.png')

	elif len(text) > 0 and len(text) < 130:

		img.write_text_box((100, 200), text, box_width=350, font_filename=font,
			font_size=25, color=color, place='center')
		img.write_text((250, 400), 'Author : '+author, font_filename=font_2,
	               font_size=15, max_height=150, color=color)

		img.save('sample-imagetext.png')

