from SinglePattern import *
from MultiplePatterns import *

def resultSP(singlePattern):
    singlePattern.train()
    print("The number of neuron's inputs=" + str(singlePattern.N))
    print("Training step=" + str(singlePattern.eta))
    print("The number of training epochs=" + str(singlePattern.K))
    print("Desired output=1")
    print("Computed output=" + str(singlePattern.computeSum(singlePattern.inputs, singlePattern.weights)))

if __name__ == '__main__':
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



    