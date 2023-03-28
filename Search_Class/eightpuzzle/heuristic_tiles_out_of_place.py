from agents.heuristic import Heuristic
from eightpuzzle.eight_puzzle_problem import EightPuzzleProblem
from eightpuzzle.eight_puzzle_state import EightPuzzleState


class HeuristicTilesOutOfPlace(Heuristic[EightPuzzleProblem, EightPuzzleState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: EightPuzzleState) -> float:
        h = 0
        for row in range(state.rows):
            for col in range(state.columns):
                if state.matrix[row][col] != 0 and state.matrix[row][col] != self._problem.goalState.matrix[row][col]:
                    h += 1
        return h

    def __str__(self):
        return "Tiles out of place"
