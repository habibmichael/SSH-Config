import os.path
import subprocess
import time
import sys
import re


#Checking IP address file and content validity
def ip_is_valid():
	check=False
	global ip_list

	while True:
		#Prompt User for input
		print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # \n"
		ip_file=raw_input("# Enter IP file name and extension: ")
		print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # \n"

		
		try:#Catch wrong file name 

			selected_ip_file=open(ip_file,'r')
			#Start from the Beginning of the file
			selected_ip_file.seek(0)
			#Reach each line , save as list
			ip_list=selected_ip_file.readlines()
			selected_ip_file.close()

		except IOError:
			print "\n* File %s does not exist! Please check and try again!\n"%ip_file

		#Octet Check 
		for ip in ip_list:
			octet_check_ip=ip.split('.')
			#Unicast address check, exclude reserved ip addresses
			if((len(octet_check_ip)==4) and (1<=int(octet_check_ip[0])<=223) and (int(octet_check_ip[0])!=127) and (int(octet_check_ip[0])!=169 or int(octet_check_ip[1])!=254) and (0<=int(octet_check_ip[1])<=255) and (0<=int(octet_check_ip[2])<=255) and (0<=int(octet_check_ip[3])<=255)):
				check=True
				break
			else:#redirect to top of while loop
				print "\nThe IP address is INVALID! Please retry!\n"
				check=False
				continue

		#Evaluate Check flag
		if check==False:
			continue
		elif check==True:
			break

	#Check IP reachability
	print "\n* Checking IP reachability. Please wait...\n"
	check2=False

	while True:
		for ip in ip_list:
			ping_reply=subprocess.call(['ping','-c','2','-w','2','-q','-n',ip])
			if ping_reply==0:
				check2=True
				continue
			elif ping_reply==2:
				print "\n* No response from device %s"%ip
				check2=False
				break
			else:
				print"\n Ping to the following device has FAILED:",ip
				check2=False
				break

		if check2==False:
			print"\n*Please re-check IP address list or device.\n"
			ip_is_valid()
		elif check2==True:
			print"\n*All devices are reachable. Waiting for username/password file...\n"
			break

#Checking username/password file
def user_is_valid():
	global user_file
	while True:
		#Prompt for username/password file
		print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # \n"
		user_file=raw_input("# Enter user/pass file name and extension: ")
		print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # \n"

		#Validate File existence 
		if os.path.isfile(user_file)==True:
			print"\n Username/Password file has been validated. Waiting for cmand file...\n"
			break
		else:
			print "\n File %s does not exist. Please check and try again!\n"%user_file
			continue

#Checking command file
def cmd_is_valid():
	global cmd_file
	while True:
		#Prompt for command file
		print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # \n"
		user_file=raw_input("# Enter command file name and extension: ")
		print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # \n"

		#Validate File existence 
		if os.path.isfile(cmd_file)==True:
			print"\n Command file has been validated. Waiting for cmand file...\n"
			break
		else:
			print "\n File %s does not exist. Please check and try again!\n"%cmd_file
			continue

#Call functions, wrapped in try/except blocks
try:
	ip_is_valid()
except KeyboardInterrupt:
	print "\n\n* Program aborted by user. Exiting...\n"
	sys.exit()

try:
	user_is_valid()
except KeyboardInterrupt:
	print "\n\n* Program aborted by user. Exiting...\n"
	sys.exit()

try:
	cmd_is_valid()
except KeyboardInterrupt:
	print "\n\n* Program aborted by user. Exiting...\n"
	sys.exit()








