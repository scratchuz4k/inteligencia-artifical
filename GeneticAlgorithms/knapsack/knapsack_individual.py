from ga.individual_bit_vector import BitVectorIndividual


class KnapsackIndividual(BitVectorIndividual):

    def __init__(self, problem: "KnapsackProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.weight = None
        self.value = None

    def compute_fitness(self) -> float:
        self.weight = 0
        self.value = 0
        for i in range(self.num_genes):
            if self.genome[i]:
                self.weight += self.problem.knapsack_items[i].weight
                self.value += self.problem.knapsack_items[i].value

        match self.problem.fitness_type:
            case self.problem.SIMPLE_FITNESS:
                self.fitness = self.value if self.weight <= self.problem.maximum_weight else 0
            case self.problem.PENALTY_FITNESS:
                penalty = 0 if self.weight <= self.problem.maximum_weight else self.problem.max_vp * (
                            self.weight - self.problem.maximum_weight)
                self.fitness = self.value - penalty

        return self.fitness

    def __str__(self):
        string = '\nWeight: ' + f'{self.weight}' + '(Max weight: ' + f'{self.problem.maximum_weight}' + ')'
        string += '\nValue: ' + f'{self.value}'
        string += '\nFitness: ' + f'{self.fitness}'
        string += '\nItems: '
        for i in range(self.num_genes):
            if self.genome[i]:
                string += str(self.problem.knapsack_items[i])
        return string

    def better_than(self, other: "KnapsackIndividual") -> bool:
        return True if self.fitness > other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.weight = self.weight
        new_instance.value = self.value
        return new_instance
