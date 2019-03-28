from SinglePattern import *
from MultiplePatterns import *

def resultSP(singlePattern, expectValue=1):
    singlePattern.train(0,1,0,1,expectValue)
    print("The number of neuron's inputs=" + str(singlePattern.N))
    print("Training step=" + str(singlePattern.eta))
    print("The number of training epochs=" + str(singlePattern.K))
    print("Desired output=1")
    print("Computed output=" + str(singlePattern.computeSum(singlePattern.inputs, singlePattern.weights)))

def resultMP(multiplePatterns, boostExpectValue=1):
    multiplePatterns.train(0,1,0,1,boostExpectValue)
    print("The number of neuron's inputs=" + str(multiplePatterns.N))
    print("The number of training patterns=" + str(multiplePatterns.M))
    print("Training step=" + str(multiplePatterns.eta))
    print("The number of training epochs=" + str(multiplePatterns.K))
    print("Desired output:")
    print(multiplePatterns.z)
    print("Computed output:")
    print(multiplePatterns.computeSumForAll(multiplePatterns.inputs, multiplePatterns.weights))

if __name__ == '__main__':

    print("SinglePattern:")
    print("TEST 1:")
    resultSP(SinglePattern())
    print("\nTEST 2:")
    resultSP(SinglePattern(100,0.01,50))
    print("\nTEST 3:")
    resultSP(SinglePattern(5,0.01,50))
    print("\nTEST 4:")
    resultSP(SinglePattern(100,0.01,5))
    print("\nTEST 5:")
    resultSP(SinglePattern(100,0.1,50))
    print("\nTEST 6:")
    resultSP(SinglePattern(100,0.1,50))

    print("\n\nMultiplePatterns:")
    print("TEST 1:")
    resultMP(MultiplePatterns())
    print("\nTEST 2:")
    resultMP(MultiplePatterns(5,5,0.01,500))
    print("\nTEST 3:")
    resultMP(MultiplePatterns(50,5,0.01,50))
    print("\nTEST 4:")
    resultMP(MultiplePatterns(500,5,0.01,50))
    print("\nTEST 5:")
    resultMP(MultiplePatterns(50,5,0.1,500))
    print("\nTEST 6:")
    resultMP(MultiplePatterns(50,5,0.01,500),20)
    