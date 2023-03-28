import numpy as np

from agents.heuristic import Heuristic
from eightpuzzle.eight_puzzle_problem import EightPuzzleProblem
from eightpuzzle.eight_puzzle_state import EightPuzzleState


class HeuristicTileDistance(Heuristic[EightPuzzleProblem, EightPuzzleState]):

    def __init__(self):
        super().__init__()
        self._lines_goal_matrix = None
        self._cols_goal_matrix = None

    def compute(self, state: EightPuzzleState) -> float:
        h = 0
        for row in range(state.rows):
            for col in range(state.columns):
                if state.matrix[row][col] != 0:
                    h += abs(row - self._line)
        return h

    def build_aux_array(self):
        pass

    @property
    def problem(self):
        return self._problem

    @problem.setter
    def problem(self, problem: EightPuzzleProblem):
        self._problem = problem
        self.build_aux_arrays()

    def __str__(self):
        return "Tiles distance to final position"

    def build_aux_arrays(self) -> None:
        goal_matrix = self._problem.goal_state.matrix
        lines_goal_matrix = []
        cols_goal_matrix = []
        for i in range(9):
            position = np.where(goal_matrix == i)
            lines_goal_matrix.append(position[0][0])
            cols_goal_matrix.append(position[1][0])
        self._lines_goal_matrix = np.array(lines_goal_matrix)
        self._cols_goal_matrix = np.array(cols_goal_matrix)
