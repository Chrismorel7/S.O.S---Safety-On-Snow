import led
import log
from time import sleep
import falldetection as fd
import getrequest as gre
import threading
import Wifilib


loop = True
FD = fd.FallDetection()
LED = led.led(40)
interface = "wlan0"
ssid = "Safety-On-Snow"

#------------------------------------------------

Wifilib.connect_to_wifi(interface, ssid)

#------------------------------------------------

LED.turnoff()
LED.blink(1, 5)

#----------------------------------------------

def main_loop():
    LED.turnon()
    while loop:
        if FD.fallsensor() == 1:
            log.log(filepath='Data/history.log', message=str(FD.PredictSeries))
            gre.send('http://192.168.1.130:8000/fall?=1')
            sleep(3)
            LED.blink(0.1, 200)
            LED.turnon()
        else:
            pass


server_thread = threading.Thread(target=gre.run_serveur)
server_thread.daemon = True
server_thread.start()
print('Serveur démarré')

main_loop()