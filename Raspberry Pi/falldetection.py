import neuralnetwork as nn
import RPi.GPIO as GPIO
import numpy as np
from sense_hat import SenseHat
from time import sleep
import datetime as dt

class FallDetection(object):
    def __init__(self):
        self.neuralnetwork = nn.NeuralNetwork(input_size=0)
        self.TrainMaxSeries = np.loadtxt("Data/inputmax.txt")
        self.TrainMinSeries = np.loadtxt("Data/inputmin.txt")
        
        self.sense = SenseHat()
        self.sense.set_imu_config(False, True, True)
        
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.default = (0,0,0)
        self.g = 9.81
        
        self.sense.clear(self.default)
        
        self.accel = None
        self.accx = None
        self.accy = None
        self.accz = None
        self.gyro = None
        self.gyrx = None
        self.gyry = None
        self.gyrz = None
        
        self.array = None
        self.array2 = None
        
        self.PredictSeries = None
        
    def getdata(self):
        self.accel = self.sense.get_accelerometer_raw()
        self.accx = round(self.accel['x'], 3) * self.g
        self.accy = round(self.accel['y'], 3) * self.g
        self.accz = round(self.accel['z'], 3) * self.g
    
        self.gyro = self.sense.get_gyroscope_raw()
        self.gyrx = round(self.gyro['x'], 3)
        self.gyry = round(self.gyro['y'], 3)
        self.gyrz = round(self.gyro['z'], 3)
    
        return np.array([self.accx, self.accy, self.accz, self.gyrx, self.gyry, self.gyrz])
    

    def getdeltadata(self, time_delta: float):
        self.array = self.getdata()
        sleep(time_delta)
        self.array2 = self.getdata()
        return np.array(self.array2 - self.array)
    
    
    def fallsensor(self):
            self.PredictSeries = self.getdeltadata(0.001)
            self.PredictSeries = np.absolute(self.PredictSeries)
            PredictSeriesArranged = (self.PredictSeries - self.TrainMinSeries) / (self.TrainMaxSeries - self.TrainMinSeries)

            fall = self.neuralnetwork.predict(PredictSeriesArranged)
    
            if fall < 0.5:
                return 0
        
            else:
                return 1