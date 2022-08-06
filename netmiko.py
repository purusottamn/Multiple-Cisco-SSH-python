#!/usr/bin/python3

#import ConnectHandler
from netmiko import ConnectHandler
#import Getpass
from getpass import getpass

#Get username
username = input("Enter your username: ')

#Get Password
password = getpass("Enter your password: ')

#Specificy device type, this scripts is written for the Cisco IOS switches only
device = {
  'device_type': 'cisco_ios',
  'username': username,
  'password': password, 
}

#open the source file where configuration are store. This file must be saved in same folder with the scripts
#see config.txt
with open('config.txt') as f:
  lines = f.read().splitlines()
print(lines)
print("")

#define the list of all devices where the config will be applied to. 
#host_list.txt file must be saved in same folder. this file contains the IP address of the devices
#see host_list_txt
all-devices = open("host_list.txt")

#applied the config file and print the output
for item in all_devices:
  device['ip] = item.strip("\n")
  net_connect = Connecthandler(**device)
  output = net_connect.send_config_set(lines)
  print(output)
  
