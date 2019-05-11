from GeneticAlgorithm import *


def function1(value):
    return value * math.sin(10 * math.pi * value) + 1

def function2(value):
    return (math.exp(value) * math.sin(10 * math.pi * value) + 1) / value

if __name__ == '__main__':
    print("GeneticAlgorithm:")

    a = 0.5
    b = 2.5

    pop_size = 5
    precision = 3

    pc = 0.25
    pm = 0.01
    epochs = 10

    genetic = GeneticAlgorithm(function2, a, b, precision)
    #genetic.draw_basic_function()
    genetic.perform(pop_size, pc, pm, epochs)