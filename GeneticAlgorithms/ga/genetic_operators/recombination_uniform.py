from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual
from ga.genetic_algorithm import GeneticAlgorithm


class RecombinationUniform(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        for i in range(len(ind1.genome)):
            if GeneticAlgorithm.rand.random() > 0.5:
                ind1.genome[i], ind2.genome[i] = ind2.genome[i], ind1.genome[i]
        pass

    def __str__(self):
        return "Uniform recombination (" + f'{self.probability}' + ")"
