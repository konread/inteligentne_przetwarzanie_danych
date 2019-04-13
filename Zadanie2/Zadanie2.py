from FileManager import *
from Neuron import *

train = FileManager()
train.read("trainFile.txt")

test = FileManager()
test.read("testFile.txt")

test2 = FileManager()
test2.read("testFile2.txt")

neuron = Neuron()
arrayOfNeurons = neuron.createArrayOfNeurons(train.numberOfTrainingPatterns)

print("#TEST CASE 1")
for idx in range(train.numberOfTrainingPatterns):
    sign, pattern = train.signsWithPatterns[idx]
    arrayOfNeurons[idx].train(pattern)

for idx in range(train.numberOfTrainingPatterns):
    sign, pattern = test.signsWithPatterns[idx]
    print("Compare " + str(sign) + " with " + str(sign) + " = " + str(arrayOfNeurons[idx].computeSum(pattern)))

print("#TEST CASE 2")
sign, pattern = test.signsWithPatterns[0]
for idx in range(len(arrayOfNeurons)):
    trainSign, trainPattern = train.signsWithPatterns[idx]
    print("Compare " + str(sign) + " with " + str(trainSign) + " = " + str(arrayOfNeurons[idx].computeSum(pattern)))