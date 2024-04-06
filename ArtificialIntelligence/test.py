import neuralnetwork as nn
import numpy as np
neuralnetwork = nn.NeuralNetwork(input_size=0)

TrainMaxSeries = np.loadtxt("inputmax.txt")
TrainMinSeries = np.loadtxt("inputmin.txt")

PredictSeries = np.abs([40.97841726618705,-0.6306954436450845,-47.43645083932854,0.31522896698615543,-1.1970181043663473,-0.021299254526091604])
PredictSeries = (PredictSeries - TrainMinSeries) / (TrainMaxSeries - TrainMinSeries)

neuralnetwork.predict(PredictSeries)