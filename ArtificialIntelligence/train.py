"""Program file to train our AI
    """

import pandas as pd
import numpy as np
import neuralnetwork as nn

ITERATION = 1_000_000

df = pd.read_csv("DataSet/csvFiles/Final/trainingdata.csv")

TrainingDF = df.drop(axis=1, columns={"index"})

training_inputdf = TrainingDF.drop(axis=1, columns="fall")
training_outputdf = TrainingDF['fall'].to_frame()

training_inputdf = np.absolute(training_inputdf)
print(training_inputdf.describe())

np.savetxt("ArtificialIntelligence/Data/inputmax.txt", np.amax(training_inputdf, axis=0), fmt="%s")
np.savetxt("ArtificialIntelligence/Data/inputmin.txt", np.amin(training_inputdf, axis=0), fmt="%s")

training_inputdf = (training_inputdf - np.amin(training_inputdf, axis=0)) / (np.amax(training_inputdf, axis=0) - np.amin(training_inputdf, axis=0))

print(training_inputdf.head())
print(training_inputdf.describe())

print("\n")
print(training_outputdf.head())

neuralnetwork = nn.NeuralNetwork(len(training_inputdf.axes[1]))

for i in range(ITERATION):
    print("\n\n\n ITERATION : ", i, "\n\n\n")
    neuralnetwork.train(training_inputdf, training_outputdf)
    
neuralnetwork.sauvegardePoids()
print("Poids sauvegardé")

TrainMaxSeries = np.loadtxt("ArtificialIntelligence/Data/inputmax.txt")
TrainMinSeries = np.loadtxt("ArtificialIntelligence/Data/inputmin.txt")
print(TrainMaxSeries, TrainMinSeries)

PredictSeries1 = np.abs([0.6546762589928061,-2.7122302158273373,0.8129496402877696,-0.05537806176783833,0.024494142705005308,-0.09371671991480302])
PredictSeries1 = (PredictSeries1 - TrainMinSeries) / (TrainMaxSeries - TrainMinSeries)

PredictSeries2 = np.abs([-87.17266187050359,98.71702637889689,-18.446043165467632,-4.795527156549522,-12.207667731629385,-18.82108626198083])
PredictSeries2 = (PredictSeries2 - TrainMinSeries) / (TrainMaxSeries - TrainMinSeries)

neuralnetwork.predict(PredictSeries1)
print("Expected result : 0\n")
neuralnetwork.predict(PredictSeries2)
print("Expected result : 1\n")