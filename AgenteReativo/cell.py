

class Cell:

    def __init__(self, line=0, column=0):
        self.line = line
        self.column = column
        self.has_wall = False
        self.dirty = False
        self.agent = None
        # Eliminar esta linha na versão para as aulas
        self.last_iteration = 0

    @property
    def color(self) -> str:
        if self.has_agent():
            return 'red'
        if self.has_wall:
            return 'blue'
        if self.dirty:
            return 'gray'
        return 'white'

    def has_agent(self) -> bool:
        return self.agent is not None

    def set_agent(self, agent) -> None:
        self.agent = agent
        if self.has_agent():
            # Eliminar esta linha na versão para as aulas
            self.last_iteration = agent.iteration + 1
            if self.dirty:
                self.dirty = False

    def __str__(self) -> str:
        if self.has_wall:
            return '#'
        elif self.has_agent():
            return 'X'
        else:
            '.'
