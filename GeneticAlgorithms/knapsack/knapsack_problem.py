
from ga.problem import Problem
from knapsack.knapsack_individual import KnapsackIndividual
from knapsack.knapsack_item import KnapsackItem


class KnapsackProblem(Problem):

    SIMPLE_FITNESS = 0
    PENALTY_FITNESS = 1

    def __init__(self, knapsack_items: list, maximum_weight: float, prob1s: float):
        self.knapsack_items = knapsack_items
        self.maximum_weight = maximum_weight
        self.prob1s = prob1s
        self.fitness_type = self.SIMPLE_FITNESS
        self.max_vp = self.compute_max_vp()

    def generate_individual(self) -> "KnapsackIndividual":
        new_individual = KnapsackIndividual(self, len(self.knapsack_items))
        new_individual.initialize(self.prob1s)
        return new_individual

    def __str__(self):
        string = "# of items: "
        string += f'{len(self.knapsack_items)}'
        string += "\nWeight limit: "
        string += f'{self.maximum_weight}'
        string += "\nItems:"
        string += "\nId\tWeight\tValue"
        for item in self.knapsack_items:
            string += f'{item}'
        return string

    def compute_max_vp(self) -> float:
        max_vp = self.knapsack_items[0].value / self.knapsack_items[0].weight
        num_items = len(self.knapsack_items)
        for i in range(1, num_items):
            div_vp = self.knapsack_items[i].value / self.knapsack_items[i].weight
            if div_vp > max_vp:
                max_vp = div_vp
        return max_vp


def build_knapsack(filename: str) -> KnapsackProblem:
    knapsack_items = []
    with open(filename, 'r') as file:
        tokens = file.readline().strip().split()
        num_items, maximum_weight = int(tokens[0]), int(tokens[1])
        for i in range(0, num_items):
            tokens = file.readline().strip().split()
            knapsack_items.append(KnapsackItem(str(i + 1), float(tokens[0]), float(tokens[1])))

    return KnapsackProblem(knapsack_items, maximum_weight, 0.5)
