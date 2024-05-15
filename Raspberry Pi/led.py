import RPi.GPIO as GPIO
from time import sleep

class led(object):
    def __init__(self, port: int):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        self.LED = port
        GPIO.setup(self.LED,GPIO.OUT)

    def turnoff(self):
        GPIO.output(self.LED,GPIO.HIGH)
    

    def turnon(self):
        GPIO.output(self.LED,GPIO.LOW)

    def blink(self, timeout: float, repetition: int):
        for i in range(repetition):
            self.turnon()
            sleep(timeout)
            self.turnoff()
            sleep(timeout)