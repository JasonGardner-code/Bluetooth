#!/usr/bin/env python3

import subprocess

def scan_bluetooth_devices():
    print("Scanning for Bluetooth devices...")
    result = subprocess.run(['bettercap', '-X', 'ble.recon'], capture_output=True)
    output = result.stdout.decode()
    print(output)

def exploit_vulnerabilities():
    print("Exploiting vulnerabilities...")
    result = subprocess.run(['bettercap', '-X', 'set ble.recon.exploits true'], capture_output=True)
    output = result.stdout.decode()
    print(output)

def capture_traffic():
    print("Capturing Bluetooth traffic...")
    result = subprocess.run(['bettercap', '-X', 'ble.sniff on'], capture_output=True)
    output = result.stdout.decode()
    print(output)

def main():
    scan_bluetooth_devices()
    exploit_vulnerabilities()
    capture_traffic()

if __name__ == "__main__":
    main()