"""Artificial intelligence training programme"""

import numpy as np

class NeuralNetwork(object):
    """Artificial Intelligence's Neural Network code"""
    def __init__(self):
        self.InputSize = None
        self.HiddenSize = None
        self.OutputSize = 1
        self.W1 = np.random.randn(self.InputSize, self.HiddenSize)
        self.W2 = np.random.randn(self.HiddenSize, self.OutputSize)

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def sigmoidprime(self, x):
        return x*(1-x)

    def forward(self, TRAIN_CONST):
        self.z = np.dot(TRAIN_CONST, self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        OutputAI = self.sigmoid(self.z3)
        return OutputAI

    def backward(self, TRAIN_CONST, CONST_OUTPUT, OutputAI):
        self.OutputError = CONST_OUTPUT - OutputAI
        self.OutputDelta = self.OutputError * self.sigmoidprime(OutputAI)
        self.z2Error = self.OutputDelta.dot(self.W2.T)
        self.z2Delta = self.z2Error * self.sigmoidprime(self.z2)
        self.W1 += TRAIN_CONST.T.dot(self.z2Delta)
        self.W2 += self.z2.T.dot(self.OutputDelta)

    def train(self, TRAIN_CONST, CONST_OUTPUT):
        OutputAI = self.forward(TRAIN_CONST)
        self.backward(TRAIN_CONST, CONST_OUTPUT, OutputAI)

    def predict(self, TRAIN_CONST):
        print("Donnée prédite après entrainement de l'IA : ")
        print("Entrée : \n" + str(TRAIN_CONST))
        print("Sortie : \n" + str(self.forward(TRAIN_CONST)))

        if self.forward(TRAIN_CONST) < 0.5:
            print("Il n'y a pas de chute ! \n")
        else:
            print("Il y a une chute ! \n")
