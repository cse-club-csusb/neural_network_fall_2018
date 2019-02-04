_author = ["Sagar Patel", "Hugo Romero" "Quimpie Tuada", "Eugene Kim","Joseph Premdas", "Mike Chang Godinez", "Mario Victorino" ]
import numpy as np
import pandas

# this training data consist of three int RGB values
training_data = ([233,100,199],[133,110,211],[201,155,99])
# the expected results only changes the last two values by dropping the left digit
expected_results = ([233,00,99],[133,10,11],[201,55,9])



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
        
