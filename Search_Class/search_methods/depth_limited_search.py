
from search_methods.depth_first_search import DepthFirstSearch
from search_methods.node import Node
from search_methods.solution import Solution
from agents.problem import Problem


class DepthLimitedSearch(DepthFirstSearch):

    def __init__(self, limit: int = 28):
        super().__init__()
        self.limit = limit

    def graph_search(self, problem: Problem) -> Solution:
        # TODO
        pass

    def __str__(self):
        return "Limited depth first search"
