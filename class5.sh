#!/bin/bash

# Script: Ops 301 Class 05 Ops Challenge Solution
# Author: sujan thapa magar           
# Date of latest revision: 02SEP2022      
# Purpose: Writes a script that clears the contents of logs and prints to the screen the before and after of the contents

# Main

# Defines vars
syslogVary=/var/log/syslog
wtmpVary=/var/log/wtmp

#Defines funct

function clear_log {
    contents
}

clear_log() {
    cat $1
    cat /dev/null > $1
    cat $1
}

# Main

clear_log $syslogVar
clear_log $wtmpVar

# End
