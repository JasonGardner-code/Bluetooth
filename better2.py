#!/usr/bin/env python3

import subprocess

def scan_bluetooth_devices():
    result = subprocess.run(['bettercap', '-X', 'ble.recon'], capture_output=True)
    output = result.stdout.decode()
    print(output)

def main():
    scan_bluetooth_devices()

if __name__ == "__main__":
    main()