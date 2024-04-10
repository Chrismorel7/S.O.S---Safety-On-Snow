import neuralnetwork as nn
import numpy as np
neuralnetwork = nn.NeuralNetwork(input_size=0)

TrainMaxSeries = np.loadtxt("inputmax.txt")
TrainMinSeries = np.loadtxt("inputmin.txt")

PredictSeries = np.abs([-0.0263788968824929,0.0359712230215825,0.0095923261390891,0.0,0.0021299254526092,-0.002129925452609])
PredictSeries = (PredictSeries - TrainMinSeries) / (TrainMaxSeries - TrainMinSeries)

neuralnetwork.predict(PredictSeries)