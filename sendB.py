from scapy.layers.bluetooth import *
from scapy.all import *

def send_bluetooth_packet(dest_addr):
    # Craft a Bluetooth inquiry packet
    bt_inquiry = Bluetooth_HCI_Hdr() / Bluetooth_HCI_Command() / Bluetooth_HCI_Inquiry()
    
    # Set the destination address
    bt_inquiry[Bluetooth_HCI_Command].opcode = 0x0401
    bt_inquiry[Bluetooth_HCI_Inquiry].LAP = 0x9e8b33
    bt_inquiry[Bluetooth_HCI_Inquiry].length = 0x30
    bt_inquiry[Bluetooth_HCI_Inquiry].num_responses = 0xff
    
    # Send the Bluetooth packet
    sendp(bt_inquiry, iface="YOUR_INTERFACE")

if __name__ == "__main__":
    bluetooth_device_address = "TARGET_BLUETOOTH_ADDRESS"
    send_bluetooth_packet(bluetooth_device_address)