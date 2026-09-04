# MicroPython Wi-Fi Network Scanner

[![MicroPython](https://img.shields.io/badge/MicroPython-2E6B8A?logo=micropython&logoColor=white)](https://micropython.org/)
[![ESP32](https://img.shields.io/badge/ESP32--S3-000000?logo=espressif&logoColor=white)](https://www.espressif.com/)

A lightweight, real-time Wi-Fi network scanner written in MicroPython for **ESP32**, **ESP8266**, and **ESP32-S3** (including the N16R8 variant). Perfect for wardriving, network diagnostics, or simply checking available Wi-Fi in your area.

## ✨ Features

- 📶 **Real-time scanning** – updates every 10 seconds.
- 📊 **Signal sorting** – shows the strongest networks first.
- 🔒 **Security detection** – identifies `Open`, `WEP`, `WPA-PSK`, `WPA2-PSK`, and `WPA/WPA2-PSK`.
- 🕵️ **Hidden SSID detection** – shows `<Hidden>` instead of a blank name.
- 🖥️ **Clean console output** – easy-to-read formatted results.
- 🛑 **Graceful exit** – press `Ctrl+C` to stop safely and disable Wi-Fi.

## 🛠️ Hardware Requirements

- Any board running **MicroPython** with Wi-Fi:
  - ESP32 / ESP32-S2 / ESP32-S3 (e.g., ESP32-S3-N16R8)
  - ESP8266
  - Raspberry Pi Pico W (with `network` module)
- USB cable for power and serial connection.
- Terminal software (Thonny, `mpremote`, `screen`, or `puTTY`).

## 🚀 Getting Started

### 1. Install MicroPython
Flash the latest MicroPyton firmware for your board:
- [Official MicroPython Downloads](https://micropython.org/download/)

### 2. Upload the script
Save the code as `main.py` or `wifi_scanner.py` on your board using:
```bash
mpremote cp wifi_scanner.py :main.py
```
Or use **Thonny** → Save As → MicroPython Device.

### 3. Run the scanner
If saved as `main.py`, it will run automatically on boot. Otherwise, run:
```python
import wifi_scanner
```
Or execute it directly in the REPL.

## 📋 Example Output

```
============================================================
Nearby Wi-Fi Networks
============================================================

(1)
SSID     : Home_5G
BSSID    : a4:77:33:1b:2c:3d
Channel  : 6
RSSI     : -45
Security : WPA2-PSK

(2)
SSID     : Office_Visitor
BSSID    : b2:55:11:9a:8b:7c
Channel  : 11
RSSI     : -58
Security : WPA/WPA2-PSK

(3)
SSID     : <Hidden>
BSSID    : c8:91:22:0e:f1:2a
Channel  : 1
RSSI     : -72
Security : Open
```

## 📂 Code Structure

```python
import network, time

# Wi-Fi station interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Security type mapping
Security = {0: "Open", 1: "WEP", 2: "WPA-PSK", 3: "WPA2-PSK", 4: "WPA/WPA2-PSK"}

# Helper: convert BSSID bytes to MAC string
def bssid_to_str(bssid):
    return ":".join("{:02x}".format(x) for x in bssid)

# Main scanning loop with error handling and keyboard interrupt
try:
    while True:
        # Print header
        print("\n" + "="*60)
        print("Nearby Wi-Fi Networks")
        print("="*60)

        try:
            networks = wlan.scan()
            if not networks:
                print("No networks found.")
            else:
                # Sort by RSSI (strongest first)
                networks.sort(key=lambda x: x[3], reverse=True)

                for i, net in enumerate(networks, start=1):
                    ssid = net[0].decode("utf-8", "ignore")
                    if not ssid: ssid = "<Hidden>"
                    bssid = bssid_to_str(net[1])
                    channel, rssi, auth = net[2], net[3], net[4]

                    print(f"\n({i})")
                    print("SSID     :", ssid)
                    print("BSSID    :", bssid)
                    print("Channel  :", channel)
                    print("RSSI     :", rssi)
                    print("Security :", Security.get(auth, f"UNKNOWN ({auth})"))
        except Exception as e:
            print("Scan Error:", e)

        time.sleep(10)

except KeyboardInterrupt:
    print("\nScan stopped by user.")
    wlan.active(False)
```

## 🔧 Customization

- **Change scan interval** – modify `time.sleep(10)` to any value in seconds.
- **Add more security types** – extend the `Security` dictionary. For example:
  - `5: "WPA3-PSK"`
  - `6: "WPA3-SAE"`
- **Save results to a file** – import `machine` and write to a `.txt` or `.csv` on the flash/PSRAM.

## 🤝 Contributing

Feel free to fork, open issues, or submit pull requests for improvements like:
- Web-based output via a captive portal.
- Deep sleep mode for battery-powered wardriving.
- Logging to an SD card or cloud.

## 📜 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute it for both personal and commercial purposes.
