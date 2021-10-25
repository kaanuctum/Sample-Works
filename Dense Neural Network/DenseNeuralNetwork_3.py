#neural network version 7
#changes from the previous version
#can oparete with n number of layers
#but each number of layer increases the amount
#of training the net needs

#DenseNeuralNetwork_2 : can now save and load the trained results

#DenseNeuralNEtwork_3 : can now implement softmax
  #for exmples where the nn has to pick one of the options, the function softmax turns the
  #outputs in to a set of probibility




#NEEDS TO BE DONE
#have to implement dropout to avoid overfitting

import numpy as np
from random import randint
import pickle
from softmax import *


def sigmoid(x):
  return 1 / (1 + np.exp(-x))


def dsigmoid(y) :
  # return sigmoid(x) * (1 - sigmoid(x))
  return y * (1 - y)
5

def dimchange(lst):
    #if the lst is a single number, the length can't be defined
    #the try tries to negate that problem
    output = list()
    try:
        for i in range(len(lst)):
            q = list()
            q.append(lst[i])
            output.append(q)
    except:
        q = list()
        q.append(lst)
        output.append(q)
    return output

class NeuralNetwork :
    def __init__(self, input_nodes, hidden_nodes, output_nodes, lr=0.1, layers=2, softmax = False):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = lr
        self.layers = layers
        self.softmax = softmax
        self.A = list()
        self.W = list()
        self.B = list()

        #create the weights
        self.weights_i = np.random.rand(self.hidden_nodes, self.input_nodes)
        self.weights_h = np.random.rand(self.hidden_nodes, self.hidden_nodes)
        self.weights_o = np.random.rand(self.output_nodes, self.hidden_nodes)

        #add the weights in to the list of weights
        self.W.append(self.weights_i)
        for i in range(self.layers - 2):
            self.W.append(self.weights_h)
        self.W.append(self.weights_o)

        #create the biases
        self.bias_h = np.random.rand(self.hidden_nodes, 1)
        self.bias_o = np.random.rand(self.output_nodes, 1)

        #add the biases in the list of biases
        for i in range(self.layers-1):
            self.B.append(self.bias_h)
        self.B.append(self.bias_o)


    def help(self):
      print("the function 'train' takes in a list of inputs")
      print('in the form of an np array with the colloms as the')
      print('individual examples and the lenght of the rows')
      print('as the number of examples in the training set')
      print('\n')
      print("after being trained, the function 'predict' takes")
      print('in a single input, and outputs the label that the')
      print('network thinks this given input should have ')


    def predict(self, input_array):
        self.A = list()
        if input_array is np.array : self.A.append(input_array)
        else: self.A.append(np.asarray(dimchange(input_array)))

        for i in range(self.layers):
          Z_n = np.dot(self.W[i],self.A[i])+self.B[i]
          A_n = sigmoid(Z_n)
          self.A.append(A_n)
        if self.softmax == True:
          self.A[-1] = softmax(self.A[-1])
        return self.A[-1].tolist()

    def train(self, inputs, targets):
        self.A = list()
        Y = targets
        n,m = Y.shape

        self.A.append(inputs)

        for i in range(self.layers):
          Z_n = np.dot(self.W[i],self.A[i])+self.B[i]
          A_n = sigmoid(Z_n)
          self.A.append(A_n)



        if self.softmax == True:
          self.A[-1] = softmax(self.A[-1])

        dz_n = self.A[self.layers] - Y
        dw_n = (np.dot(dz_n, np.transpose(self.A[self.layers - 1])))/m
        db_n = (np.sum(dz_n, axis=1, keepdims=True))/m
        self.W[self.layers -1] -= (self.learning_rate * dw_n)
        self.B[self.layers -1] -= (self.learning_rate * db_n)

        for i in range(self.layers-1):
          q = self.layers-i-1
          dz_n = np.dot(np.transpose(self.W[q]), dz_n) * dsigmoid(self.A[q])
          dw_n = (np.dot(dz_n, np.transpose(self.A[q-1])))/m
          db_n = (np.sum(dz_n, axis=1, keepdims=True))/m
          self.W[q-1] -= (self.learning_rate * dw_n)
          self.B[q-1] -= (self.learning_rate * db_n)
    
    def load(self, file_name):
      file_name = str(file_name)
      with open('{}.pkl'.format(file_name),'rb') as f:  # Python 3: open(..., 'rb')
        self.W, self.B = pickle.load(f)
      

    def save(self, file_name):
      file_name = str(file_name)
      with open('{}.pkl'.format(file_name), 'wb') as f:
        pickle.dump([self.W, self.B], f)      

    # outputs.print()
    # targets.print()
    # error.print()





