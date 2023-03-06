from action import Action
from cell import Cell
from perception import Perception


class ReactiveAgent:

    def __init__(self, cell: Cell):
        self.iteration = 0
        self.environment = None
        self.cell = cell
        cell.set_agent(self)

    def act(self, environment) -> None:
        perception = self.build_perception(environment)
        action = self.decide(perception)
        self.execute(action, environment)
        self.iteration += 1

    def set_cell(self, new_cell: Cell) -> None:
        self.cell.set_agent(None)
        self.cell = new_cell
        self.cell.set_agent(self)

    def build_perception(self, environment) -> Perception:
        return Perception(environment.get_north_cell(self.cell), environment.get_south_cell(self.cell),
                          environment.get_east_cell(self.cell), environment.get_west_cell(self.cell))

    def decide(self, perception: Perception) -> Action:
        # return self.decide_a(perception)
        # return self.decide_b(perception)
        # return self.decide_c(perception)
        return self.decide_d(perception)

    def execute(self, action: Action, environment) -> None:
        next_cell = None

        if action == Action.NORTH and environment.has_north_cell(self.cell):
            next_cell = environment.get_north_cell(self.cell)
        elif action == Action.SOUTH and environment.has_south_cell(self.cell):
            next_cell = environment.get_south_cell(self.cell)
        elif action == Action.EAST and environment.has_east_cell(self.cell):
            next_cell = environment.get_east_cell(self.cell)
        elif action == Action.WEST and environment.has_west_cell(self.cell):
            next_cell = environment.get_west_cell(self.cell)

        if next_cell is not None and not next_cell.has_wall and not next_cell.has_agent():
            self.set_cell(next_cell)

    def decide_a(self, perception: Perception):

        # Implement the decision process of a basic version of the reactive agent,
        # which should simply wander around the world avoiding hitting the walls.
        # This agent doesn’t care about dirt, yet (but it always cleans visited
        # cells on this and the next exercises).

        if perception.n is not None and not perception.n.has_wall:
            return Action.NORTH
        if perception.e is not None and not perception.e.has_wall:
            return Action.EAST
        if perception.s is not None and not perception.s.has_wall:
            return Action.SOUTH
        if perception.w is not None and not perception.w.has_wall:
            return Action.WEST

    def decide_b(self, perception: Perception):

        # The agent should now be able to perceive dirt in adjacent
        # cells and use that information in its decision process.
        # This agent prefers to visit dirty cells first.

        if perception.n is not None and perception.n.dirty:
            return Action.NORTH
        if perception.e is not None and perception.e.dirty:
            return Action.EAST
        if perception.s is not None and perception.s.dirty:
            return Action.SOUTH
        if perception.w is not None and perception.w.dirty:
            return Action.WEST
        return None

    def decide_c(self, perception: Perception):

        # Implement a memory mechanism that allows the agent to prefer
        # visiting cells that were visited the longest. Your goal is that
        # the agent visits as many cells as possible. This agent doesn’t
        # care about dirt. You may need to change the Cell class...

        action = None
        olderIt = 99999

        self.cell.last_iteration = self.iteration

        if perception.n is not None and not perception.n.has_wall:
            olderIt = perception.n.last_iteration
            action = Action.NORTH

        if perception.e is not None and not perception.e.has_wall and olderIt > perception.e.last_iteration:
            olderIt = perception.e.last_iteration
            action = Action.EAST

        if perception.s is not None and not perception.s.has_wall and olderIt > perception.s.last_iteration:
            olderIt = perception.s.last_iteration
            action = Action.SOUTH

        if perception.w is not None and not perception.w.has_wall and olderIt > perception.w.last_iteration:
            olderIt = perception.w.last_iteration
            action = Action.WEST

        return action

    def decide_d(self, perception: Perception):

        # Finally, implement a decision process in which the agent, besides
        # preferring to visit dirty cells first, it prefers to visit cells that
        # were visited the longest. It should consider the second criterium as a
        # tiebreaker, when more than one adjacent cell is dirty or if there are
        # no dirty adjacent cells.

        action = self.decide_b(perception)

        if(action is None):
            action = self.decide_c(perception)

        return action
