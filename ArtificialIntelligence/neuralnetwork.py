"""Artificial intelligence training programme"""

import numpy as np
import pandas as pd

class NeuralNetwork(object):    
    """Artificial Intelligence's Neural Network code"""
    def __init__(self, input_size: int):
        self.input_size = input_size
        self.hidden_size = input_size + 1
        self.output_size = 1
        self.w1 = np.random.randn(self.input_size, self.hidden_size)
        self.w2 = np.random.randn(self.hidden_size, self.output_size)
        self.z = None
        self.z2 = None
        self.z3 = None
        self.output_error = None
        self.output_delta = None
        self.z2_error = None
        self.z2_delta = None

    def ReLu(self, x):
        """Fonction ReLu"""
        return np.where(x > 0, x, 0)

    def ReLuprime(self, x):
        """Fonction derivée de la fonction ReLu"""
        return np.where(x > 0, 1, 0)

    def forward(self, training_input):
        """Fonction d'entrainement avec la méthode forward"""        
        self.z = np.dot(training_input, self.w1)
        
        print("\nTraining_input : ", pd.DataFrame(training_input).head())
        print(pd.DataFrame(training_input).describe())
        print("\nW1 : ", pd.DataFrame(self.w1).head())
        print(pd.DataFrame(self.w1).describe())
        print("\nZ : ", pd.DataFrame(self.z).head())
        print(pd.DataFrame(self.z).describe())
        
        self.z2 = self.ReLu(self.z)
        
        print("\nZ2 : ", pd.DataFrame(self.z2).head())
        print(pd.DataFrame(self.z2).describe())
        
        self.z3 = np.dot(self.z2, self.w2)

        print("\nZ3 : ", pd.DataFrame(self.z3).head())
        print(pd.DataFrame(self.z3).describe())
        
        ai_output = self.ReLu(self.z3)
        
        print("\nAI Output : ", pd.DataFrame(ai_output).head())
        print(pd.DataFrame(ai_output).describe())
        
        return ai_output

    def backward(self, training_input, training_output, ai_output):
        """Fonction d'entrainement avec la méthode backward"""
        self.output_error = training_output - ai_output
        self.output_delta = self.output_error * self.ReLuprime(ai_output)
        self.z2_error = self.output_delta.dot(self.w2.T)
        self.z2_delta = self.z2_error * self.ReLuprime(self.z2)
        self.w1 += training_input.T.dot(self.z2_delta)
        self.w2 += self.z2.T.dot(self.output_delta)

    def train(self, training_input, training_output):
        """Fonction d'entrainement du model"""
        ai_output = self.forward(training_input)
        self.backward(training_input, training_output, ai_output)

    def predict(self, predictingseries):
        """Fonction de prediction du résultat"""
        print("\nDonnée prédite après entrainement de l'IA : ")
        print("\nEntrée : \n" + str(predictingseries))
        print("\nSortie : \n" + str(self.forward(predictingseries)))

        if self.forward(predictingseries) < 0.5:
            print("Il n'y a pas de chute ! \n")
        else:
            print("Il y a une chute ! \n")
