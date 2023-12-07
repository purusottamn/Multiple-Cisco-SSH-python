#!/usr/bin/python3

# Import libraries
from netmiko import ConnectHandler, NetMikoTimeoutException, AuthenticationException
from getpass import getpass
from threading import Thread, Lock

# Define device information
device_type = 'cisco_ios'

# Define functions
def connect_and_apply_config(device_ip, username, password, lines, lock):
  try:
    # Connect to device
    device = {'device_type': device_type, 'ip': device_ip, 'username': username, 'password': password}
    net_connect = ConnectHandler(**device)

    # Apply configuration
    output = net_connect.send_config_set(lines)

    # Lock output to avoid conflict
    with lock:
      print('\n' + '-' * 150)
      print(f"Output from {device_ip}:\n")
      print(output)

    net_connect.disconnect()
  except AuthenticationException:
    with lock:
      print(f"Authentication failure for {device_ip}")
  except NetMikoTimeoutException:
    with lock:
      print(f"Timeout from device: {device_ip}")
  except EOFError:
    with lock:
      print(f"End of file reached: {device_ip}")
  except:
    with lock:
      print(f"Unexpected error for {device_ip}")

# Get user credentials
print("\nPlease enter your credentials!\n")
username = input('Enter your username: ')
password = getpass('Enter your password: ')

# Define configuration lines and device list
with open('config.txt') as f:
  lines = f.read().splitlines()

with open("host_list.txt") as f:
  devices = [item.strip("\n") for item in f]

# Initialize lock and thread list
lock = Lock()
threads = []

# Start thread for each device
for device_ip in devices:
  thread = Thread(target=connect_and_apply_config, args=(device_ip, username, password, lines, lock))
  thread.start()
  threads.append(thread)

# Wait for all threads to finish
for thread in threads:
  thread.join()

print("All devices processed!")
