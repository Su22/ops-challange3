#!/bin/bash

# Script: Ops 301 Class 04 Ops Challenge Solution
# Author: sujan thapa magar              
# Date of latest revision: 01SEP2022      
# Purpose: Menu system with options that do different things and does not end until the user selects exit

# Main

PS3="select one of the following menu options: "

select number in Print_Hello_World Ping_Loopback Print_IP_Information Exit 
do 
    case $number in
        Print_Hello_World) 
        echo "----------------------------"
        echo "Hello World"
        echo "----------------------------"
        ;;
        Ping_Loopback)
        echo "----------------------------"
        echo "loopback ping: "
        ping -c 5 192.168.0.4
        echo "----------------------------"
        ;;
        Print_IP_Information)
        echo "----------------------------"
        echo "computer's IP informaion: "
        echo "----------------------------"
        ifconfig
        ;;
        Exit)
        echo "----------------------------"
        echo "done!"
        exit

    esac
done

# End
