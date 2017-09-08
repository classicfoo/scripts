#!/usr/bin/env python3

import time
import sys
import subprocess
import os

#get filepath arguments separated by spaces
files = ' '.join(sys.argv[1:])

today = time.strftime("%Y-%b-%d").upper()

#get archive name
archiveName = today + ".tar.gz"

def archive():
	#run bash command
	#https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
	bashCommand = "tar czvf " + archiveName + " " + files
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

	print("\"{}\" was archived!".format(files));

#if no archive exists create one
if(not os.path.exists(archiveName)):
	archive()

#if archive does not exist, ask if user wants to overwrite? else cancel.
else:
	print("Archive named \"{}\" already exists!".format(archiveName))
	overwrite = input("Do you wish to overwrite (y/n)? ")
	if(overwrite == "y"):
		archive()
	else:
		print("Backup aborted!");

