#!/bin/bash

# Check if bettercap is running
if pgrep -x "bettercap" > /dev/null
then
    echo "bettercap is running"
else
    echo "Starting bettercap..."
    bettercap &
fi

# Set Uber tooth device to discoverable mode
hciconfig hci0 piscan

# Scan for nearby Bluetooth devices and extract the MAC address of the Uber tooth device
mac_address=$(hcitool scan | grep "Uber tooth" | awk '{ print $1 }')

# Check if the Uber tooth is connected
if hcitool con | grep "Uber tooth" > /dev/null
then
    echo "Uber tooth is connected"
else
    if [ -n "$mac_address" ]
    then
        echo "Trying to connect to Uber tooth..."
        hcitool cc $mac_address
    else
        echo "Uber tooth MAC address not found. Please make sure the device is in discoverable mode."
    fi
fi
