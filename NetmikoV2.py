!/usr/bin/python3

#import ConnectHandler
from netmiko import ConnectHandler
#import timeout Exception
from netmiko.ssh_exception import NetMikoTimeoutException
#import Authentication Exception 
from netmiko.ssh_exception import AuthenticationException
#import Getpass
from getpass import getpass

# Get Username
print ("\nPlease enter your credentials!\n")
username = input('\nEnter your username: ')

#Get password
password =getpass('Enter your password: ')

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
print("")

#define the list of all devices where the config will be applied to. 
#host_list.txt file must be saved in same folder. this file contains the IP address of the devices
#see host_list.txt
all-devices = open("host_list.txt")

#applied the config file and print the output
print((" Checking devices..."))
print("")
for item in all_devices:
    device['ip'] = item.strip("\n")
    try:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_set(lines)
        print("\n", '-' *150)
        print(output)
        print("")
    except (Authenticationexception):
        print("Authentication Failure: " + item)
        continue
    except (NetmikoTimeoutException):
        print("\n", '-' *150)
        print("Time out from device: " + item)
        continue
    except (EOFError):
        print("\n", '-' *150)
        print("End of File reached: " + item)
        continue
    except KeyboardInterrupt:
        print("\nScript Terminated manually! \n")
        raise systemExit
       
        
