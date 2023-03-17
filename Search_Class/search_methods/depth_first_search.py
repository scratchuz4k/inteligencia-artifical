
from utils.node_queue import NodeQueue
from search_methods.graph_search import GraphSearch
from search_methods.node import Node
from search_methods.solution import Solution
from agents.problem import Problem
from agents.state import State


class DepthFirstSearch(GraphSearch[NodeQueue]):

    def __init__(self):
        super().__init__(NodeQueue)

    def graph_search(self, problem: Problem) -> Solution:
        # TODO
        pass

    def add_successor_to_frontier(self, successor: State, parent: Node) -> None:
        # TODO
        pass

    def __str__(self):
        return "Depth first search"
