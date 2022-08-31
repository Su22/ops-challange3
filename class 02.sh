#!/bin/bash

# Script: Ops 301 
# Author: sujan thapa magar 
# Date of latest revision: 8/30/2022
# Purpose: Copies log to working directory and appends the current date and time to the filename

# Main

day=$(date +%D%T)

cp /var/log/syslog 

mv syslog syslog_$day

# End
