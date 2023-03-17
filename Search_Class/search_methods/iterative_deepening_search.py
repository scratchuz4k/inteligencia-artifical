
from search_methods.depth_limited_search import DepthLimitedSearch
from search_methods.search_method import SearchMethod
from search_methods.node import Node
from search_methods.solution import Solution
from agents.problem import Problem


class IterativeDeepeningSearch(DepthLimitedSearch):

    # We do not use the code from DepthLimitedSearch because we can optimize
    # so that the algorithm only verifies if a state is a goal if its depth is
    # equal to the limit. Note that given a limit X we are sure not to
    # encounter a solution below this limit because a (failed) limited depth
    # search has already been done. That's why we do not extend this class from
    # DepthLimitedSearch. We extend from DepthFirstSearch so that we don't need
    # to rewrite method insertSuccessorsInFrontier again.
    # After the class, please see a version of the search algorithm without
    # this optimization.

    def search(self, problem: Problem) -> Solution:
        self.reset()
        self.num_generated_states = 0  # Specific to this algorithm
        self.stopped = False
        self.limit = 0

        # TODO

    def graph_search(self, problem: Problem) -> Solution:
        # TODO
        pass

    def __str__(self):
        return "Iterative deepening search"


#########################################################


class NonOptimizedIterativeDeepeningSearch(SearchMethod):

    def search(self, problem: Problem) -> Solution:
        depth_limited_search = DepthLimitedSearch()
        i = 0
        while True:
            depth_limited_search.limit = i
            solution = depth_limited_search.search(problem)
            self.limit += 1
            if solution is not None:
                return solution
            i += 1
