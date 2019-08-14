#!/usr/bin/env python
# main.py jason amato
#000000000000000000000000000000
#-------------------------------
#set all attributes the script uses in this var - PUT A SPACE before the -  !!!!!
#ie GetSystemHWInventoryREDFISH_ja.py -a y    , then set otherattribs to "-a y"
otherattribs = " -a y"
#-------------------------------

import os
import getpass

iplist = list()
#
f = open('ipfile')
for line in f :
  ip = line.rstrip()
  ip = str(ip)
  iplist.append(ip)  

iplist = sorted(iplist)
print(f'Running on: { iplist }')

prog1 = input('Enter the program to run: ')
user1 = input('iDRAC Username: ')
pass1 = getpass.getpass('iDRAC Password: ')    

check1 = input('Are you sure you want to run this? Type Y to continue...')
if check1 == 'Y' :
   for ip1 in iplist : 
      cmdline = 'python ' + prog1 + ' -ip ' + ip1 + ' -u ' + user1 + ' -p ' + pass1 + otherattribs
      print(f"Running... { prog1 } on { ip1 }")
      os.system(cmdline)

print('Done.')
      
  
