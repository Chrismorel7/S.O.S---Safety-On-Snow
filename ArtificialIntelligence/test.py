import neuralnetwork as nn
import numpy as np
neuralnetwork = nn.NeuralNetwork(input_size=0)

TrainMaxSeries = np.loadtxt("ArtificialIntelligence/Data/inputmax.txt")
TrainMinSeries = np.loadtxt("ArtificialIntelligence/Data/inputmin.txt")

PredictSeries = np.abs([1.3337044,
                        0.34323275,
                        8.5710121,
                        0.43,
                        0.906,
                        0.132])
PredictSeries = (PredictSeries - TrainMinSeries) / (TrainMaxSeries - TrainMinSeries)

neuralnetwork.predict(PredictSeries)