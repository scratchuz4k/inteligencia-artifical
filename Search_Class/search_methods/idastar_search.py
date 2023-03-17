
import sys

from search_methods.iterative_deepening_search import IterativeDeepeningSearch
from search_methods.node import Node
from search_methods.solution import Solution
from agents.problem import Problem
from agents.state import State


class IDAStarSearch(IterativeDeepeningSearch):

    # This algorithm is a hybrid: it is an informed algorithm, but it is based on the
    # Iterative Deepening Algorithm(IDA).
    # That's why we make it a subclass of IterativeDeepeningSearch class instead of the InformedSearch one:
    # it uses a NodeQueue instead of a NodePriorityQueue.
    # Despite the fact that it is based on IDA, we don't reuse any code of it because all methods
    # (search, search_graph and add_successor_to_frontier) have their particularities.
    # Note that, on each  iteration, the search is done in a depth first search way.

    def __init__(self):
        super().__init__()
        self.heuristic = None
        self.new_limit = 0

    def search(self, problem: Problem) -> Solution:
        self.reset()
        self.stopped = False

        # TODO

    def graph_search(self, problem: Problem) -> Solution:
        # TODO
        pass

    def add_successor_to_frontier(self, successor: State, parent: Node) -> None:
        # TODO
        pass

    def __str__(self):
        return "IDA Star search"
