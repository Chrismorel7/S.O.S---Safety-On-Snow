"""Program file to train our AI
    """

import pandas as pd
import numpy as np
import neuralnetwork as nn

ITERATION = 20000

df = pd.read_csv("DataSet/csvFiles/test.csv")

df = np.round(df)
print(df.head(10))

TrainingDF = df.drop(axis=1, columns={"newindex", "index", "date"})

training_inputdf = TrainingDF.drop(axis=1, columns="fall")
training_outputdf = TrainingDF['fall'].to_frame()

print(training_inputdf.head())
print("\n")
print(training_outputdf.head())

neuralnetwork = nn.NeuralNetwork(len(training_inputdf.axes[1]))

for i in range(ITERATION):
    print("\n\n\n ITERATION : ", i, "\n\n\n")
    neuralnetwork.train(training_inputdf, training_outputdf)
    
neuralnetwork.predict([13.83453237410072,
                       -68.81534772182255,
                       -51.302158273381295,
                       13.87220447284345,
                       13.794462193823216,
                       3.288604898828541,])