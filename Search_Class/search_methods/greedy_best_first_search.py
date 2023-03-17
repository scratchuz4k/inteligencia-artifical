
from search_methods.informed_search import InformedSearch
from search_methods.node import Node
from agents.state import State


class GreedyBestFirstSearch(InformedSearch):

    # f = h
    def add_successor_to_frontier(self, successor: State, parent: Node) -> None:
        # TODO
        pass

    def __str__(self):
        return "Greedy best first search"
