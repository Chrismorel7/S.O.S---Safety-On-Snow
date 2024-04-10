import neuralnetwork as nn
import numpy as np
neuralnetwork = nn.NeuralNetwork(input_size=0)

TrainMaxSeries = np.loadtxt("inputmax.txt")
TrainMinSeries = np.loadtxt("inputmin.txt")

PredictSeries = np.abs([-42.37649880095923,
                        88.58033573141486,
                        28.06235011990408,
                        1.887113951011714,
                        -0.2939297124600646,
                        -12.562300319488818])
PredictSeries = (PredictSeries - TrainMinSeries) / (TrainMaxSeries - TrainMinSeries)

neuralnetwork.predict(PredictSeries)