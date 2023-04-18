
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination
from ga.genetic_algorithm import GeneticAlgorithm


class RecombinationOneCut(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        cut = GeneticAlgorithm.rand.randint(0, ind1.num_genes)
        for i in range(cut):
            ind1.genome[i], ind2.genome[i] = ind2.genome[i], ind1.genome[i]

    def __str__(self):
        return "One cut recombination (" + f'{self.probability}' + ")"
