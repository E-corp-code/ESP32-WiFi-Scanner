# ESP32 Advanced Wi-Fi Recon Tool v2.0

[![MicroPython](https://img.shields.io/badge/MicroPython-2E6B8A?logo=micropython&logoColor=white)](https://micropython.org/)
[![ESP32](https://img.shields.io/badge/ESP32--S3-000000?logo=espressif&logoColor=white)](https://www.espressif.com/)
[![Version](https://img.shields.io/badge/Version-2.0-blue.svg)](https://github.com/E-corp-code/ESP32-WiFi-Scanner)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An enterprise-grade, tactical Wi-Fi reconnaissance and black-box logging tool written in MicroPython for **ESP32**, **ESP8266**, and **ESP32-S3** (specifically optimized for the N16R8 variant). Designed for wardriving, hardware auditing, and local wireless intelligence gathering.

---

## ✨ What's New in v2.0

- 🔍 **Hardware Fingerprinting (Vendor OUI Lookup)** – Automatically parses the first 3 bytes of a router's MAC address (BSSID) to identify the hardware manufacturer (e.g., Apple, TP-Link, Cisco, Espressif).
- 💾 **Flash Memory CSV Logging** – Seamlessly writes all scan results directly to a persistent `wifi_log.csv` file on the ESP32’s flash memory with custom timestamps and sanitized strings.
- 🛡️ **Sanitized Data Handling** – Strips commas and invalid characters from SSIDs to ensure clean spreadsheet and database imports.

---

## 🚀 Core Features

- 📶 **Real-time Airspace Scanning** – Continuous loop tracking nearby wireless traffic.
- 📊 **Signal Strength Sorting** – Automatically prioritizes networks by RSSI (strongest signal first).
- 🔒 **Comprehensive Security Detection** – Identifies `Open`, `WEP`, `WPA-PSK`, `WPA2-PSK`, `WPA/WPA2-PSK`, and `WPA3-PSK`.
- 🕵️ **Hidden SSID Handling** – Gracefully flags cloaked networks as `<Hidden>`.
- 🛑 **Graceful Interrupts** – Safely tears down the network interface and clears buffers on `Ctrl+C`.

---

## 🛠️ Hardware Requirements

- **Microcontroller:** ESP32, ESP32-S2, or ESP32-S3 (Recommended: **ESP32-S3-N16R8** with 16MB Flash / 8MB PSRAM).
- **Firmware:** Latest [MicroPython Firmware](https://micropython.org/download/).
- **Interface:** USB cable for power and serial telemetry.
- **Environment:** Thonny IDE, `mpremote`, or any standard serial terminal (`puTTY`, `screen`).

---

## 📦 Installation & Deployment

### 1. Flash MicroPython
Ensure your board is running the latest MicroPython firmware.

### 2. Upload the Code
Save the script as `main.py` directly to the device root using `mpremote`:
```bash
mpremote cp main.py :main.py
