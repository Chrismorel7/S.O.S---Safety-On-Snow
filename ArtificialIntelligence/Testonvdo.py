import neuralnetwork as nn
import pandas as pd
import numpy as np

output = pd.DataFrame()
input = pd.read_csv('DataSet/csvFiles/csvDelta/Input_vdo11015_delta.csv')
input = input.drop(axis=1, columns={"oldindex", "fall"})

NN = nn.NeuralNetwork()
TrainMaxSeries = np.loadtxt("inputmax.txt")
TrainMinSeries = np.loadtxt("inputmin.txt")

output = NN.forward(input)
outputfall = output[output['fall'] == 1.0]

print(outputfall)