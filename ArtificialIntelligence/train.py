"""Program file to train our AI
    """

import pandas as pd
import numpy as np
import neuralnetwork as nn

ITERATION = 1000

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
    print(pd.DataFrame(neuralnetwork.ai_output).describe())
    print(pd.DataFrame(neuralnetwork.output_error).describe())
    
neuralnetwork.predict([-5.661870503597123,-0.5419664268585132,-19.429256594724222,-2.2492012779552715,1.919062832800852,-1.8562300319488816])

neuralnetwork.predict([-78.24940047961631,-53.33093525179856,78.5779376498801,-0.8402555910543131,19.64856230031949,3.4195953141640043])

print(pd.DataFrame(neuralnetwork.w2))