#get storage chassis enclosure info

 

import requests, json, sys, re, time, os, warnings, argparse
from datetime import datetime

warnings.filterwarnings("ignore")
 

parser = argparse.ArgumentParser(description='Python script using Redfish API DMTF to get server storage enclosure info')
parser.add_argument('-ip', help='iDRAC IP Address', required=True)
parser.add_argument('-u', help='iDRAC username', required=True)
parser.add_argument('-p', help='iDRAC username pasword', required=True)
parser.add_argument('-C', help='Get chassis info, pass in \"y\"', required=False)

args=vars(parser.parse_args())

idrac_ip=args["ip"]
idrac_username=args["u"]
idrac_password=args["p"]

def get_chassis():
    response = requests.get('https://%s/redfish/v1/Chassis' % idrac_ip,verify=False,auth=(idrac_username, idrac_password))
    data = response.json()
    print("\n- Server controller(s) detected -\n")
    controller_list=[]
    for i in data[u'Members']:
        controller_list.append(i[u'@odata.id'][38:])
        print(i[u'@odata.id'][38:])

if __name__ == "__main__":
    if args["C"]:
        get_chassis()
    else:
        print("\n- WARNING, either incorrect parameter value(s) passed in or missing parameter")
