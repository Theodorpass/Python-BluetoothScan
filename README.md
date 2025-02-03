# Bluetooth Device Scanner

This Python project allows you to scan nearby Bluetooth devices and log their details such as device name, address, and RSSI (signal strength). The program uses the **`bleak`** library to discover and interact with Bluetooth devices.


## Features

- Scan nearby Bluetooth devices asynchronously.
- Display the device name, address, and RSSI of each found device.
- Logs the results with detailed information.

## Prerequisites

Before running the project, you need to have the following:

- Python 3.6 or newer installed.
- The `bleak` library to discover Bluetooth devices.

## Installation

1. Clone or download this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/bluetooth-device-scanner.git
   ```

2. Install the required dependencies from `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the project directory.

   ```bash
   cd bluetooth-device-scanner
   ```

2. Run the Python script to start scanning for Bluetooth devices.

   ```bash
   python scan_bluetooth.py
   ```

3. The script will start scanning for nearby Bluetooth devices and log the results.

## Example Output

```
INFO:root:Program started.
INFO:root:Starting Bluetooth scan...
INFO:root:Found 3 devices:
INFO:root:Device: Device_1 - AA:BB:CC:DD:EE:FF - RSSI: -75
INFO:root:Device: Device_2 - 00:11:22:33:44:55 - RSSI: -60
INFO:root:Device: Device_3 - 66:77:88:99:AA:BB - RSSI: -50
INFO:root:Program finished.
```

## Requirements

- Python 3.6 or newer.
- `bleak==0.14.0` (Bluetooth Low Energy library).

## Troubleshooting

If you encounter any issues, check the following:

- Make sure Bluetooth is enabled on your device.
- Ensure you have the latest version of the `bleak` library installed.

## License

All rights reserved.
