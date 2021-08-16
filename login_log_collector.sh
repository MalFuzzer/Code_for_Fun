#!/bin/bash

log_file="out.log"


echo "Last loggedin users:" > $log_file
last | head -n 2 >> $log_file
echo "Cross-reference data:" >> $log_file
cat /var/log/auth.log | grep ssh | tail -n 2 >> $log_file
echo "" >> $log_file
echo "IP address:" >> $log_file && ifconfig eth0 | grep -v inet6 | grep inet >> $log_file
