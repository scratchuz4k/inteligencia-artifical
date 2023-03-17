from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from agents.state import State
from agents.action import Action

S = TypeVar("S", bound=State)


class Problem(ABC, Generic[S]):

    def __init__(self, state: State):
        self.initial_state = state
        self.heuristic = None

    @abstractmethod
    def get_actions(self, state: S) -> list:
        pass

    @abstractmethod
    def get_successor(self, state: S, action: Action) -> S:
        pass

    @abstractmethod
    def is_goal(self, state: S) -> bool:
        pass

    def compute_path_cost(self, path: list) -> int:
        cost = 0
        for action in path:
            cost += action.cost
        return cost
