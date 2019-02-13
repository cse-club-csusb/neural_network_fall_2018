_author = ["Sagar Patel", "Hugo Romero" "Quimpie Tuada", "Eugene Kim","Joseph Premdas", "Mike Chang Godinez", "Mario Victorino" ]
import numpy as np
import pandas

# this training data consist of three int RGB values
training_data = np.array(([233,100,199],[133,110,211],[201,155,99]), dtype=float)
# the expected results only changes the last two values by dropping the left digit
expected_results = np.array ([[233,00,99],[133,10,11],[201,55,9]],dtype=float)

np.random.seed(1)


# test
class Neural_Network(object):
    def __init__(self):
         self.inputsize  = 3             # number of neurons is choosen by
         self.outputsize = 1             # Nh =       Ns
         self.hidden_size = 1            #      ______________
                                         #     (a * (Ni + No))  a = scaling factor h = hidden, i = input, o = output, s = samples in data set
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
        
