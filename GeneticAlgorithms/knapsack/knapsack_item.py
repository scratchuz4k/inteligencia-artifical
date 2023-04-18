
class KnapsackItem:

    def __init__(self, name: str, weight: float, value: float):
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return "\n" + self.name + "\t" + f'{self.weight}' + "\t" + f'{self.value}'
