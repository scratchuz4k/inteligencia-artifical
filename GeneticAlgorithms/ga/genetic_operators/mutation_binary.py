from random import Random

from ga.individual_bit_vector import BitVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_algorithm import GeneticAlgorithm


class MutationBinary(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, individual: BitVectorIndividual) -> None:
        for i in range(len(individual.genome)):
            if GeneticAlgorithm.rand.Random() < self.probability:
                individual.genome[i] = not individual.genome[i]

    def __str__(self):
        return "Binary mutation (" + f'{self.probability}' + ")"
