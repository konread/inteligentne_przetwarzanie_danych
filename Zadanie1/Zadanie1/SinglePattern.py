import random
import numpy as np

class SinglePattern(object):
    # N - the number of neuron's inputs
    # eta - training step
    # K - the number of training epochs
    def __init__(self, N=10, eta=0.01, K=500):
        self.N = N
        self.eta = eta
        self.K = K
        self.realNumbersPrecision = 3

    # desired output
    def train(self, minWeightRange = 0, maxWeightRange = 1, minInputRange = 0, maxInputRange = 1, z = 1):
        self.weights = [round(random.uniform(minWeightRange, maxWeightRange), self.realNumbersPrecision) for _ in range(self.N)]
        self.inputs = [round(random.uniform(minInputRange, maxInputRange), self.realNumbersPrecision) for _ in range(self.N)]
        self.errors = []

        for _ in range(self.K):
            y = 0
            for xi, wi in zip(self.inputs, self.weights):
                y += xi * wi
            
            self.errors.append(y)
            for idx, value in enumerate(self.weights):
                self.weights[idx] = value + self.eta * (z - y) * self.inputs[idx]

        return self