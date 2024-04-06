import neuralnetwork as nn
import numpy as np
neuralnetwork = nn.NeuralNetwork(input_size=0)

TrainMaxSeries = np.loadtxt("inputmax.txt")
TrainMinSeries = np.loadtxt("inputmin.txt")

PredictSeries = np.abs([5.02877697841727,1.484412470023976,0.0,4.43024494142705,10.233226837060704,-6.9850905218317365])
PredictSeries = (PredictSeries - TrainMinSeries) / (TrainMaxSeries - TrainMinSeries)

neuralnetwork.predict(PredictSeries)