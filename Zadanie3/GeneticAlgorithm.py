import math
import numpy
import matplotlib.pyplot as plt
import random


class GeneticAlgorithm(object):

    def __init__(self, function, left_value_range, right_value_range, precision):
        self.function = function
        self.left_value_range_a = left_value_range
        self.right_value_range_b = right_value_range
        self.values_range = numpy.arange(self.left_value_range_a, self.right_value_range_b, 0.01)
        self.max_chromosome_number = 100
        self.precision = precision

    def draw_basic_function(self):
        x_axis_value = []
        y_axis_value = []

        for value in self.values_range:
            x_axis_value.append(value)
            y_axis_value.append(self.function(value))

        plt.grid()
        plt.plot(x_axis_value, y_axis_value)
        plt.show()

    def count_chromosome_bits_number(self, precision):
        subintervals = int((self.right_value_range_b - self.left_value_range_a) * (10**precision))

        exponent = 1
        for exponent_temp in range(1, self.max_chromosome_number):
            new_value = 2 ** exponent_temp
            if new_value > subintervals:
                exponent = exponent_temp
                break

        return exponent

    def create_chromosome(self, chromosome_bits_number):
        chromosome = []
        for _ in range(1, chromosome_bits_number+1):
            chromosome.append(random.randint(0, 1))

        return chromosome

    def to_decimal(self, bin_array):
        result = 0
        index = 0
        for exp in reversed(range(len(bin_array))):
            result += bin_array[index] * (2**exp)
            index += 1
        return result

    def fitness(self, bin_array):
        value = self.left_value_range_a + (((self.right_value_range_b - self.left_value_range_a) * self.to_decimal(bin_array)) / ((2 ** len(bin_array)) - 1))
        return round(value, self.precision)

    def rule_method(self, chromosomes):
        fit_values = []
        total_adjustment = 0
        for chromosome in chromosomes:
            value = self.function(self.fitness(chromosome))
            fit_values.append(value)
            total_adjustment += value

        probability = []
        for value in fit_values:
            if total_adjustment == 0:
                print("")
            probability.append(value / total_adjustment)

        distribution = []
        distribution.append(probability[0])
        for index in range(1, len(probability)):
            distribution.append(distribution[index-1] + probability[index])

        new_population = []
        for _ in range(len(distribution)):
            random_value = random.uniform(0, 1)
            for distributionIdx in range(len(distribution)):
                if distribution[distributionIdx] > random_value:
                    tempIdx = distributionIdx-1
                    if tempIdx > 0:
                        new_population.append(chromosomes[tempIdx])
                        break
                    else:
                        new_population.append(chromosomes[0])
                        break

        return new_population

    def create_new_population(self, pop_size, precision):
        chromosome_bits_number = self.count_chromosome_bits_number(precision)
        chromosomes = []

        for _ in range(1, pop_size+1):
            chromosomes.append(self.create_chromosome(chromosome_bits_number))

        return chromosomes

    def crossover(self, bin_array1, bin_array2):
        position = random.randint(0, len(bin_array1)-2)
        for index in range(position, len(bin_array1)):
            t = bin_array1[index]
            bin_array1[index] = bin_array2[index]
            bin_array2[index] = t

    def perform_crossbreeding(self, chromosomes, pc):
        for idx in range(len(chromosomes)):
            random_value = random.uniform(0, 1)
            if random_value < pc:
                new_index = random.randint(0, len(chromosomes)-1)
                self.crossover(chromosomes[idx], chromosomes[new_index])

    def mutation(self, chromosomes, pm):
        for loopIdx in range(len(chromosomes)):
            for idx in range(len(chromosomes[loopIdx])):
                random_value = random.uniform(0, 1.01)
                if random_value < pm:
                    chromosomes[loopIdx][idx] = 1 - chromosomes[loopIdx][idx]

    def eval_function(self, chromosomes):
        max_values = []
        for loopIdx in range(len(chromosomes)):
            max_values.append(self.fitness(chromosomes[loopIdx]))
        return max(max_values)

    def find_max_with_idx(self, values):
        idx = 0
        value = values[idx]
        for index in range(1, len(values)):
            if values[index] > value:
                value = values[index]
                idx = index
        return idx, value

    def perform(self, new_population, pc, pm, epochs):
        values = []
        for i in range(1, epochs):
            new_population = self.rule_method(new_population)
            self.perform_crossbreeding(new_population, pc)
            self.mutation(new_population, pm)
            values.append(self.eval_function(new_population))

        idx, value = self.find_max_with_idx(values)
        print("W pokoleniu " + str(idx) + " pojawil sie najlepszy chromosom Xmax = " + str(value))

        plt.plot(values)
        plt.show()