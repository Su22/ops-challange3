#!/usr/bin/python3

# Script: Ops 301 Class 12 Ops Challenge Solution
# Author: sujan thapa magar                  
# Date of latest revision: 14SEP2022      
# Purpose: Psutil fetches the following information:
# Import psutil
import psutil

# Main
print(psutil.cpu_times())
print(psutil.cpu_freq())
print(psutil.net_io_counters())

# End
