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
ip_is_valid()


