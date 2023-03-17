
from utils.node_priority_queue import NodePriorityQueue
from search_methods.graph_search import GraphSearch
from search_methods.node import Node
from agents.state import State


class UniformCostSearch(GraphSearch[NodePriorityQueue]):

    def __init__(self):
        super().__init__(NodePriorityQueue)

    # f = g
    def add_successor_to_frontier(self, successor: State, parent: Node) -> None:
        # TODO
        pass

    def __str__(self):
        return "Uniform cost search"
