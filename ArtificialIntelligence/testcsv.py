import neuralnetwork as nn
import pandas as pd
import numpy as np

NN = nn.NeuralNetwork(input_size=0)

input = pd.read_csv('DataSet/csvFiles/Test/Input_vdo21064_delta.csv')
input = input.drop(axis=1, columns={"oldindex", "fall"})
print(pd.DataFrame(input).describe())

TrainMaxSeries = np.loadtxt("ArtificialIntelligence/Data/inputmax.txt")
TrainMinSeries = np.loadtxt("ArtificialIntelligence/Data/inputmin.txt")
print(pd.DataFrame(TrainMaxSeries).describe)
print(pd.DataFrame(TrainMinSeries).describe)


inputbool = (input - TrainMinSeries) / (TrainMaxSeries - TrainMinSeries)
print(pd.DataFrame(inputbool).describe())
output = pd.DataFrame(NN.forward(inputbool))
#output.to_csv('Test.csv')

output = pd.read_csv("test.csv")
print(output.describe())
outputfall = output[output["fall"] == 1.0]

print(outputfall)