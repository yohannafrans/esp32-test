import gc
import network
import senko
import machine

wifi_ssid = "hm"
wifi_pass = "yohannafrans2"

def wifi_network(ssid=wifi_ssid, password=wifi_pass):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network ({})...".format(ssid))
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("network config:", sta_if.ifconfig())
    return True

def main():
    gc.collect()
    gc.enable()
    GITHUB_URL = "https://raw.githubusercontent.com/yohannafrans/esp32-test/master/example/"
    OTA = senko.Senko(GITHUB_URL, ["main.py"])
    if OTA.fetch():
        print("A newer version is available!")
        if  OTA.update():
            print("updated to the latest version! Rebooting...")
            machine.reset()
    else:
        print("Up to date!")
    
if __name__ == "__main__":
    wifi_network()
    main()