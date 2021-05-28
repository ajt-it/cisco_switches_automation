#!/usr/bin/env python
#-*- coding: utf-8 -*-

#### THIS SCRIPT IS FOR CISCO SWITCHES AUTOMATION CONFIGURATION ####

import getpass
import sys
print " "
print "Default encoding : " + sys.getdefaultencoding()
print " "
import telnetlib
import os

user = raw_input("Enter your telnet username: ")
print " "
password = getpass.getpass()
print " "

######### PRINT FILES LOCATION
cwd = os.getcwd()
print("This script and all input files are located in : ") + cwd
print " "

def banner():
        cisco_switches_automation = """\033[92m

  ____ ___ ____   ____ ___     ______        _____ _____ ____ _   _ _____ ____  
 / ___|_ _/ ___| / ___/ _ \   / ___\ \      / /_ _|_   _/ ___| | | | ____/ ___| 
| |    | |\___ \| |  | | | |  \___ \\ \ /\ / / | |  | || |   | |_| |  _| \___ \ 
| |___ | | ___) | |__| |_| |   ___) |\ V  V /  | |  | || |___|  _  | |___ ___) |
 \____|___|____/ \____\___/   |____/  \_/\_/  |___| |_| \____|_| |_|_____|____/ 
                                                                               
    _   _   _ _____ ___  __  __    _  _____ ___ ___  _   _ 
   / \ | | | |_   _/ _ \|  \/  |  / \|_   _|_ _/ _ \| \ | |
  / _ \| | | | | || | | | |\/| | / _ \ | |  | | | | |  \| |
 / ___ \ |_| | | || |_| | |  | |/ ___ \| |  | | |_| | |\  |
/_/   \_\___/  |_| \___/|_|  |_/_/   \_\_| |___\___/|_| \_|
                                                           


\033[0m"""
        return cisco_switches_automation


print banner()
print " "


## DEPEND THE IP ADDRESS DECLARED IN THE FILE - THE LOOP
## ...................... WILL CONNECT TO EACH MATERIALS.

f = open('switches_list')

for fline in f:
	print "Configuring Switch " + (fline)
	HOST = fline
	tn = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
		tn.read_until("Password: ")
		tn.write(password + "\n")

	tn.write("conf t\n")

## ... STARTING OF VLANS CONFIGURATION BY SETTING UP DESCRIPTION (NAME)
	d = open('vlans_number')

	print " "
	print "SET HERE EACH VLAN DESCRIPTION (NAME) : "
	print " "

	for dline in d:
		ID = dline
		tn.write("vlan " + str(ID) + "\n")
		while True:
			description = raw_input("Write down the name for VLAN %s" % ID)
## THE VLAN DESCRIPTION IS NECESSARY !		
			if not description:
				print "########################## Sorry, you can not leave blank! Please give a description!"
				print " "
				continue
			else:
				break
		tn.write("name " + str(description) + "\n")
		tn.write("state active\n")
		tn.write("no shut\n")
	tn.write("exit\n")
#
#
## ... HERE, WE SET EACH VLANS INTERFACES.
## ... INTERFACES WILL BE DECLARED IN "vlans_interfaces"

	n = open('vlans_interfaces')

	print " "
	print "MENTION THE 'ID NUMBER' OF EACH VLAN CORRESPONDING TO THE INTERFACE ON WHICH THE ACCESS PORT SHOULD BE CONFIGURES"
	print " "

	for nline in n:
		INT = nline
		tn.write("int gig " + str(INT) + "\n")
		tn.write("switchport mode access\n")
        while True:
			ACCESS = raw_input("Set access vlan number : ")
			if not ACCESS.isdigit():
				print "You must enter a number. Refer to file : vlans_number"
				print " "
				continue
        	else:
            	break
		tn.write("switchport access vlan " + str(ACCESS) + "\n")
		tn.write("no shut\n")
		tn.write("exit\n")
#
#
#### SETTING UP TRUNK INTERFACES ON THE SWITCH.
####
#### FIRST WE CONFIGURE INTERFACES
	x = open('vlans_trunk_interfaces')

	for xline in x:
		DOT = xline
		tn.write("int gig " + str(DOT) + "\n")
		tn.write("switchport trunk encapsulation dot1q\n")
		tn.write("switchport mode trunk\n")
#
#### SECOND WE DECLARE WHICH VLANS ARE ALLOWED TO GO TROUGHT TRUNK INTERFACES
	w = open('vlans_allowed_trunk')

	for wline in w:
		AUTH = wline
		allowed = ("vlan " + str(AUTH))
		tn.write("switchport trunk allowed " + str(allowed) + "\n")
		tn.write("no shut\n")
		tn.write("exit\n")


	tn.write("end\n")
	tn.write("wr\n")
	tn.write("exit\n")

	print tn.read_all()

print " "
print "#####################################################################################"
print "#										   #"
print "#                                   END						   #"
print "# 				      OF					   #"
print "# 					SCRIPT					   #"
print "#										   #"
print "#####################################################################################"
