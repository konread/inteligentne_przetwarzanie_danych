import random
import numpy as np
import math

class Neuron(object):
    def __init__(self):
        self.weights = []

    # desired output
    def train(self, inputs):
        self.weights = self.normalize(inputs)
        return self

    def computeSum(self, inputs):
        normalizedInputs = self.normalize(inputs)
        y=0
        for xi, wi in zip(normalizedInputs, self.weights):
            y += xi * wi
        return y

    def normalize(self, array):
        counter = self.count(array)
        newArray = []

        if counter < 1:
            return array

        for idx in range(len(array)):
            newArray.append(array[idx] / math.sqrt(counter))
        return newArray

    def count(self, array):
        counter = 0
        for item in array:
            if item == 1:
                counter = counter + 1
        return counter

    def createArrayOfNeurons(self, number):
        array =[]
        for _ in range(number):
            array.append(Neuron())
        return array