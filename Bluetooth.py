import asyncio
import logging
from bleak import discover

# Set up logging to capture any errors or unexpected behavior
logging.basicConfig(level=logging.DEBUG)

async def scan_bluetooth_devices():
    try:
        logging.info("Starting Bluetooth scan...")
        
        # Discover nearby Bluetooth devices
        devices = await discover()
        
        # Log how many devices were found
        logging.info(f"Found {len(devices)} devices:")
        
        if not devices:
            logging.warning("No devices found.")
            return
        
        for device in devices:
            logging.info(f"Device: {device.name} - {device.address} - RSSI: {device.rssi}")
    
    except Exception as e:
        logging.error(f"Error during Bluetooth scan: {e}")

if __name__ == "__main__":
    logging.info("Program started.")
    asyncio.run(scan_bluetooth_devices())
    logging.info("Program finished.")
    
    # Pause the program before it exits (for debugging)
    input("Press Enter to exit...")
