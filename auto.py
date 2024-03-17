import time
from core import scan, BluezTarget, BluezAddressType, pair, record, playback

devices = scan()

print("Found Bluetooth devices:")
for idx, device in enumerate(devices):
    print(f"{idx + 1}. {device.alias} ({device.address})")

choice = int(input("Select a device by entering the corresponding number: "))
selected_device = devices[choice - 1]

print(f"Performing actions on selected device: {selected_device.alias} ({selected_device.address})")

pair(selected_device.address, BluezAddressType.PUBLIC)
record(selected_device.address, "recording.wav")
playback("recording.wav", "alsa_output.pci-0000_00_05.0.analog-stereo")

print("Finished actions on selected device.")
