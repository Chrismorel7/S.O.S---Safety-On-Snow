"""Program file to train our AI
    """

import keyboard as kb
import pandas as pd
import numpy as np
import neuralnetwork as nn

ITERATION = 10_000_000

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

train = True
for i in range(ITERATION):
    print("\n\n\n ITERATION : ", i, "\n\n\n")
    neuralnetwork.train(training_inputdf, training_outputdf)
    
    print("Appuyez sur 'q' pour quitter...")
    while True:
        if kb.is_pressed('q'):
            print("\n\nSortie de la boucle.")
            train = False
            break
        else:
            break

    if not train:
        break
    
    
neuralnetwork.sauvegardePoids()
print("\n\n\nPoids sauvegardé\n\n\n")