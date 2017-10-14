#!/usr/bin/env python3
import datetime
import os.path

filename = datetime.date.today().strftime("%y%m%d, %a, %d %b %Y")

if not os.path.isfile(filename):
	file = open(filename ,'w')
	file.close()
else:
	print("file already exists.")


