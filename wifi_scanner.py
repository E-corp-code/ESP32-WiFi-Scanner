import network
import time
import os

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

SECURITY = {
    0: "Open", 1: "WEP", 2: "WPA-PSK",
    3: "WPA2-PSK", 4: "WPA/WPA2-PSK", 5: "WPA3-PSK"
}

OUI_DATABASE = {
    "ac:de:48": "Apple",
    "f8:ff:c2": "TP-Link",
    "24:4b:fe": "Espressif (ESP32)",
    "00:14:bf": "Cisco",
    "b8:27:eb": "Raspberry Pi",
}

LOG_FILE = "wifi_log.csv"

def bssid_to_str(bssid):
    return ":".join("{:02x}".format(x) for x in bssid)

def get_vendor(bssid_str):
    prefix = bssid_str[:8].lower()
    return OUI_DATABASE.get(prefix, "Unknown")

try:
    os.stat(LOG_FILE)
except OSError:
    with open(LOG_FILE, "w") as f:
        f.write("Timestamp,SSID,BSSID,Channel,RSSI,Security,Vendor\n")

print("[*] ESP32 Recon Tool v2.0 Started...")

try:
    while True:
        print("\n" + "="*40 + "\nScanning Airwaves...\n" + "="*40)
        networks = wlan.scan()
        
        if networks:
            networks.sort(key=lambda x: x[3], reverse=True)
            timestamp = time.time()
            
            with open(LOG_FILE, "a") as f:
                for i, net in enumerate(networks, start=1):
                    ssid = net[0].decode("utf-8", "ignore").replace(",", "") or "<Hidden>"
                    bssid = bssid_to_str(net[1])
                    channel, rssi = net[2], net[3]
                    auth = SECURITY.get(net[4], f"UNKNOWN({net[4]})")
                    vendor = get_vendor(bssid)
                    
                    print(f"({i}) {ssid} | {bssid} [{vendor}] | RSSI: {rssi}dBm")
                    f.write(f"{timestamp},{ssid},{bssid},{channel},{rssi},{auth},{vendor}\n")
                    
        time.sleep(10)
except KeyboardInterrupt:
    wlan.active(False)
    print("\n[!] Stopped by user.")
