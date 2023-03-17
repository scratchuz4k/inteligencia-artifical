
from agents.heuristic import Heuristic
from eightpuzzle.eight_puzzle_problem import EightPuzzleProblem
from eightpuzzle.eight_puzzle_state import EightPuzzleState


class HeuristicTilesOutOfPlace(Heuristic[EightPuzzleProblem, EightPuzzleState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: EightPuzzleState) -> float:
        # TODO
        pass

    def __str__(self):
        return "Tiles out of place"
