
import numpy as np
import copy
from ga.genetic_algorithm import GeneticAlgorithm
from ga.population import Population
from ga.selection_methods.selection_method import SelectionMethod
from ga.individual import Individual


class RouletteWheel(SelectionMethod):

    def run(self, population: Population) -> Population:
        new_population = Population(population.size)
        accumulated = np.full(population.size, 0, dtype=float)
        accumulated[0] = population.individuals[0].fitness
        for i in range(1, population.size):
            accumulated[i] = accumulated[i - 1] + population.individuals[i].fitness

        fitness_sum = accumulated[population.size - 1]
        if fitness_sum != 0:
            for i in range(population.size):
                accumulated[i] /= fitness_sum

        for i in range(population.size):
            new_population.individuals.append(self.roulette(population, accumulated))

        return new_population

    @classmethod
    def roulette(cls, population: Population, accumulated: np.ndarray) -> Individual:
        # Case where all individuals have fitness 0
        if accumulated[population.size - 1] == 0:
            return copy.deepcopy(population.individuals[GeneticAlgorithm.rand.randint(0, population.size - 1)])

        probability = GeneticAlgorithm.rand.random()
        for i in range(population.size):
            if probability <= accumulated[i]:
                return copy.deepcopy(population.individuals[i])

    def __str__(self):
        return "Roulette wheel selection"
