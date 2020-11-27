import gc
import network
import senko
import machine

wifi_ssid = "hm"
wifi_pass = "yohannafrans2"

def connect_wlan(ssid=wifi_ssid, password=wifi_pass):
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    ap_if.active(False)

    if not sta_if.isconnected():
        print("Connecting to WLAN ({})...".format(ssid))
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    return True

def main():
    gc.collect()
    gc.enable()

    SSID = "hm"
    PASSWORD = "yohannafrans"

    connect_wlan(SSID, PASSWORD)

    GITHUB_URL = "https://raw.githubusercontent.com/yohannafrans/esp32-test/master/example/"
    OTA = senko.Senko(GITHUB_URL, ["boot.py", "main.py"])

    if OTA.fetch():
        print("A newer version is available!")
    else:
        print("Up to date!")

    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()
    
if __name__ == "__main__":
    main()