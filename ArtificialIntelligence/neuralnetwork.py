"""Artificial intelligence training programme"""

import numpy as np

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

    def sigmoid(self, x):
        """Fonction sigmoid"""
        return 1/(1+np.exp(-x, dtype=np.float64))

    def sigmoidprime(self, x):
        """Fonction derivée de la fonction sigmoid"""
        return x*(1-x)

    def forward(self, training_input):
        """Fonction d'entrainement avec la méthode forward"""
        self.z = np.dot(training_input, self.w1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.w2)
        ai_output = self.sigmoid(self.z3)
        return ai_output

    def backward(self, training_input, training_output, ai_output):
        """Fonction d'entrainement avec la méthode backward"""
        self.output_error = training_output - ai_output
        self.output_delta = self.output_error * self.sigmoidprime(ai_output)
        self.z2_error = self.output_delta.dot(self.w2.T)
        self.z2_delta = self.z2_error * self.sigmoidprime(self.z2)
        self.w1 += training_input.T.dot(self.z2_delta)
        self.w2 += self.z2.T.dot(self.output_delta)

    def train(self, training_input, training_output):
        """Fonction d'entrainement du model"""
        ai_output = self.forward(training_input)
        self.backward(training_input, training_output, ai_output)

    def predict(self, predictingseries):
        """Fonction de prediction du résultat"""
        print("Donnée prédite après entrainement de l'IA : ")
        print("Entrée : \n" + str(predictingseries))
        print("Sortie : \n" + str(self.forward(predictingseries)))

        if self.forward(predictingseries) < 0.5:
            print("Il n'y a pas de chute ! \n")
        else:
            print("Il y a une chute ! \n")
