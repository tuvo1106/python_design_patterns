"""
Template
- Allows us to define the 'skeleton' of the algorithm, with concrete
  implementations kept in subclass

Motivation
- Algorithms can be decomposed into common parts + specifics
- Strategy pattern does this through composition
  - High-level algorithm expects strategies to conform to an interface
  - Concrete implementations implement the interface
- Template Method does the same thing through inheritance
  - Overall algorithm defined in base class; makes use of abstract members
  - Inheritors ovveride the abstract methods
  - Template method invoked to get work done
"""


from abc import ABC


class Game(ABC):

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.current_player = 0

    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f'Player {self.winning_player} wins!')

    def start(self): pass

    @property
    def have_winner(self): pass

    def take_turn(self): pass

    @property
    def winning_player(self): pass


class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turns = 10
        self.turn = 1

    def start(self):
        print(f'Starting chess with {self.number_of_players} players.')

    @property
    def have_winner(self):
        return self.turn == self.max_turns

    def take_turn(self):
        print(f'Turn {self.turn} taken by player {self.current_player}')
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player


if __name__ == '__main__':
    CHESS = Chess()
    CHESS.run()
