
from search_methods.astar_search import AStarSearch
from search_methods.node import Node
from search_methods.solution import Solution
from agents.problem import Problem


class BeamSearch(AStarSearch):

    def __init__(self, beam_size: int = 100):
        super().__init__()
        self.beam_size = beam_size

    def graph_search(self, problem: Problem) -> Solution:
        # TODO
        pass

    def manage_frontier_size(self) -> None:
        # TODO
        pass

    def __str__(self):
        return "Beam search"
