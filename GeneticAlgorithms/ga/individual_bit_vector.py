
from abc import abstractmethod
import numpy as np
from ga.problem import Problem
from ga.individual import Individual
from ga.genetic_algorithm import GeneticAlgorithm


class BitVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        self.genome = np.full(num_genes, False, dtype=bool)

    def initialize(self, prob1s: float):
        for i in range(self.num_genes):
            self.genome[i] = True if GeneticAlgorithm.rand.random() < prob1s else False

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "BitVectorIndividual") -> bool:
        pass
