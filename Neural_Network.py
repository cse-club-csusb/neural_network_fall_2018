_author = ["Sagar Patel", "Hugo Romero" "Quimpie Tuada", "Eugene Kim","Joseph Premdas", "Mike Chang Godinez", "Mario Victorino" ]
import numpy as np
import pandas

# test
class Neural_Network:
    def __init__(self):
        print("This is a Neural Network")
        
    def forward(self, x):
        o = 10
        return o
#This sigmoid fucntion follows the formula
#S(s) = 1/(1+e^-s) = e^s/(e^s + 1)
    def sigmoid(self, s):
        if s >= 0:
            z = np.exp(-s)
            return 1/(1 + z)
        else:
            z = np.exp(s)
            return z/(1 + z)

        return s

    def sigmoidPrime(self, s):
        return s
    def backward(self,X,y,o):
        print("nothing to return here")

    def train(self, X, y):
        print("nothing to return here")

    def saveWeights(self):
        print("nothing to return here")
    def predict(self):
        print("The Predict Function is coming the future")
        
