#!/usr/bin/env python3

import argparse
from core import connect, BluezTarget, BluezAddressType
import subprocess

def check_network_security():
    # Add code to check network security before attempting to connect
    result = subprocess.run(['nmap', '-sV', 'target_ip_address'], capture_output=True)
    print(result.stdout)

def main():
    parser = argparse.ArgumentParser(
        prog="Connect",
        description="Try to connect to a device using system tools",
    )
    parser.add_argument(
        "-a",
        "--target-address",
        help="Target device MAC address",
        required=True,
        dest="address",
    )
    parser.add_argument(
        "-t",
        "--target-address-type",
        help="Target device MAC address type",
        dest="address_type",
        type=lambda t: BluezAddressType[t],
        choices=list(BluezAddressType),
        default=BluezAddressType.BR_EDR,
    )
    args = parser.parse_args()

    check_network_security()  # Perform a network security check before connecting
    connect(BluezTarget(args.address, args.address_type), verbose=True)

if __name__ == "__main__":
    main()
