import os
import time
import led

LED = led.led(40)

def connect_to_wifi(interface, name):
    os.system('sudo ifconfig wlan0 down')
    time.sleep(0.5)
    os.system('sudo ifconfig wlan0 up')
    time.sleep(0.5)
    os.system('sudo iwconfig ' + interface + ' essid ' + name)
    LED.blink(1, 5)