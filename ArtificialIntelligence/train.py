"""Program file to train our AI
    """

import pandas as pd
import numpy as np
import neuralnetwork as nn

ITERATION = 100

df = pd.read_csv("DataSet/csvFiles/Input.csv")
TrainingDF = df.drop(axis=1, columns={"newindex", "index", "date"})

training_inputdf = TrainingDF.drop(axis=1, columns="fall")
training_outputdf = TrainingDF['fall'].to_frame()

print(training_inputdf.head())
print("\n")
print(training_outputdf.head())

neuralnetwork = nn.NeuralNetwork(len(training_inputdf.axes[1]))

for i in range(ITERATION):
    neuralnetwork.train(training_inputdf, training_outputdf)
    
neuralnetwork.predict([-73.54916067146283,
                       60.57314148681055,
                       -78.5779376498801,
                       15.21618743343983,
                       24.466453674121407,
                       -24.293929712460063])