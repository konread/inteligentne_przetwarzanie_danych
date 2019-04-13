from FileManager import *
from Neuron import *

train = FileManager()
train.read("trainFile.txt")

test = FileManager()
test.read("testFile.txt")

neuron = Neuron()
arrayOfNeurons = neuron.createArrayOfNeurons(train.numberOfTrainingPatterns)

for idx in range(train.numberOfTrainingPatterns):
    sign, pattern = train.signsWithPatterns[idx]
    arrayOfNeurons[idx].train(pattern)

for idx in range(train.numberOfTrainingPatterns):
    sign, pattern = test.signsWithPatterns[idx]
    print("For sign " + str(sign) + " = " + str(arrayOfNeurons[idx].computeSum(pattern)))