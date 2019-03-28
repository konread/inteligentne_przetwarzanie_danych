import random
import numpy as np

class MultiplePatterns(object):
    # N - the number of neuron's inputs
    # M - the number of training patterns
    # eta - training step
    # K - the number of training epochs
    def __init__(self, N=20, M=2, eta=0.01, K=500):
        self.N = N
        self.M = M
        self.eta = eta
        self.K = K
        self.realNumbersPrecision = 3

    # desired output
    def train(self, minWeightRange = 0, maxWeightRange = 1, minInputRange = 0, maxInputRange = 1, boostExpectValue = 1):
        self.weights = [round(random.uniform(minWeightRange, maxWeightRange), self.realNumbersPrecision) for _ in range(self.N)]
        self.inputs = []
        for _ in range(self.M):
            self.inputs.append([round(random.uniform(minInputRange, maxInputRange), self.realNumbersPrecision) for _ in range(self.N)])
        self.errors = []
        self.z = [round(boostExpectValue * random.uniform(minWeightRange, maxWeightRange), self.realNumbersPrecision) for _ in range(self.M)]

        for _ in range(self.K):
            for idxInputs, inputsValue in enumerate(self.inputs):
                errors = []
                y = self.computeSum(self.inputs[idxInputs], self.weights)
                errors.append(y)

                for idx, value in enumerate(self.weights):
                    self.weights[idx] = value + self.eta * (self.z[idxInputs] - y) * self.inputs[idxInputs][idx]

            self.errors.append(errors)

        return self

    def computeSum(self, inputs, weights):
        y=0
        for xi, wi in zip(inputs, weights):
            y += xi * wi
        return y

    def computeSumForAll(self, inputs, weights):
        result = []
        for input in inputs:
            result.append(self.computeSum(input, weights))

        return result