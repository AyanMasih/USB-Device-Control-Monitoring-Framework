# Basic USB Device Monitoring Script
# Safe for internship and learning purposes

import time
import subprocess

def get_usb_devices():
    try:
        output = subprocess.check_output(
            "wmic path Win32_USBControllerDevice get Dependent",
            shell=True
        )
        print(output.decode())
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("[+] USB Device Monitoring Started")
    print("[+] Press CTRL+C to stop")

    try:
        while True:
            get_usb_devices()
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n[!] Monitoring stopped")
