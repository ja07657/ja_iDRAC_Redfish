#!/usr/bin/env python
# main.py jason amato
#000000000000000000000000000000
#-------------------------------
#set all attributes the script uses in this var - PUT A SPACE before the -  !!!!!
#ie GetSystemHWInventoryREDFISH_ja.py -a y    , then set otherattribs to "-a y"
#otherattribs = " -a y"
otherattribs = ""
#-------------------------------

import os
import getpass
import argparse

iplist = list()
#
args = "notset" 
parser = argparse.ArgumentParser("Enter program name to be run")
parser.add_argument("-p", help="The python program to run on the iDRAC")
args = parser.parse_args()
print(args)
if args.p is not None : 
 #
 f = open('ipfile')
 for line in f :
  ip = line.rstrip()
  ip = str(ip)
  iplist.append(ip)  

 iplist = sorted(iplist)
 print(f'Running on: { iplist }')

 prog1 = str(args.p)
 user1 = input('iDRAC Username: ')
 pass1 = getpass.getpass('iDRAC Password: ')    

 check1 = input('Are you sure you want to run this? Type Y to continue...')
 if check1 == 'Y' :
   for ip1 in iplist : 
      ip1 = str(ip1)
      cmdline = 'python2 ' + prog1 + ' -ip ' + ip1 + ' -u ' + user1 + ' -p ' + pass1 + otherattribs
      print(f"Running... { prog1 } on { ip1 }")
      os.system(cmdline)

 print('Done.')
else :
 print('Please enter the program name, like so: main.py -p prog.py')
      
  
