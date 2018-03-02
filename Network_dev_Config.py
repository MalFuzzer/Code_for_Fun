# Creator: Uriel Kosayev

import re
import time
import os
import sys
import netmiko
import telnetlib

USER = ''
PASS = ''
l_telnet = []

def connect_telnet(ip):
    
    """
    connect_telnet(ip) >>> bool
    This function configures Syslog to network devices with Telnet protocol
    and creates report on devices that supports Telnet
    """
    
    # Try to connect with Telnet
    try:
        device = telnetlib.Telnet(ip)
    # The device doesn't support either SSH or Telnet   
    except:
        return False
    
    device.read_until("Username: ")
    device.write(USER + "\n")
    device.read_until("Password: ")
    device.write(PASS + "\n")

    # Telnet sucks
    time.sleep(1.5)
         
    
    try:
        msg = device.read_until("Login invalid", timeout = 1)
        if "Login invalid" in msg:
            print "Wrong credentials with Telnet"
            return False
    except:
        pass
    
	# Commands to configure in the device
    print "Connected with Telnet"
    device.write("config t" + "\n")
    device.read_until("#")
    device.write("" + "\n")
    device.read_until("#")
    device.write("" + "\n")
    device.read_until("#")
    device.write("" + "\n")
    device.read_until("#")
  
    print "Configuration commited succefully with Telnet at IP: {}\n".format(ip)

    # Report on Telnet devices
    with open(r"Telnet_devices.txt", 'a') as log:
            log.write(ip+'\n')
    return True


def connect_ssh(ip):
    
    """
    check_ssh(ip) >>> bool
    This function configures Syslog on network devices with SSH
    """

    print "Trying to connect with SSH to {}...".format(ip)

    # Trying to connect with SSH
    try:
        device = netmiko.ConnectHandler(device_type='cisco_ios', ip = ip, username = USER, password = PASS)

    # Wrong Credentials Error
    except netmiko.NetMikoAuthenticationException:
        print "Wrong Credentials (Username or Password) for SSH!\n"
        sys.exit(0)


    # sys.exit(0) means continue to next device

    # SSH disabled error
    except netmiko.NetMikoTimeoutException:
        print "SSH is disabled on {}".format(ip)
        if connect_telnet(ip) is False:
            print "Failed to connect to {} with SSH and Telnet".format(ip)
            sys.exit(0)
        else:
            return True
    except:
        sys.exit(0)

    try:
        # Entering config mode
        device.config_mode()

    # Something wrong with netmiko
    except:
        sys.exit(0)

	# Commands to configure in the device
    device.send_command("")
    device.send_command("")
    device.send_command("")

    # Exit configuration mode
    device.exit_config_mode()

    # Saves configuration
    device.send_command("wr")

    # Disconnect device
    device.disconnect()

    print "Done with {} !\n".format(ip)


def main():

    # Read all IP's
    with open(r"devices.txt", 'r') as f:
        data = f.read()

    # IP regex pattern   
    pat = r'(?:\d{1,3}\.){3}\d{1,3}'

    # Get all IP's 
    l_ip = re.findall(pat,data)
    
    for ip in l_ip:
        try:
            connect_ssh(ip)
            
        # Something wrong with the device 
        except SystemExit:
            continue
        


if __name__ == '__main__':
    main()
