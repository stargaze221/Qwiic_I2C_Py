import smbus
import time

# I2C bus number (0 or 1 for Jetson Orin Nano)
I2C_BUS = 7  # This is the default bus on most Jetson devices

# Initialize the I2C bus
bus = smbus.SMBus(I2C_BUS)

# Function to scan for devices
def scan_i2c_devices():
    print("Scanning for I2C devices...")
    devices = []
    
    for address in range(0x03, 0x99):
        try:
            bus.write_byte(address, 0)
            devices.append(hex(address))
            time.sleep(0.1)
        except IOError:
            pass
    
    if devices:
        print("Found devices at the following addresses:")
        for device in devices:
            print(device)
    else:
        print("No devices found on the I2C bus.")

if __name__ == "__main__":
    scan_i2c_devices()
