import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

Security = {
    0: "Open", 1: "WEP", 2: "WPA-PSK",
    3: "WPA2-PSK", 4: "WPA/WPA2-PSK"
}

def bssid_to_str(bssid):
    return ":".join("{:02x}".format(x) for x in bssid)

try:
    while True:
        print("\n" + "=" * 60)
        print("Nearby Wi-Fi Networks")
        print("=" * 60)
        
        try:
            networks = wlan.scan()
            
            if not networks:
                print("No networks found.")
            else:
                networks.sort(key=lambda x: x[3], reverse=True)
                
                for i, net in enumerate(networks, start=1):
                    ssid = net[0].decode("utf-8", "ignore")
                    if not ssid:
                        ssid = "<Hidden>"
                    
                    bssid = bssid_to_str(net[1])
                    channel = net[2]
                    rssi = net[3]
                    auth = net[4]
                    
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
