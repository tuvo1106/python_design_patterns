"""
Dependency Inversion Principle
- High level modules should not depend on low level ones
- Use abstractions
"""

from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


# solution
class RelationshipBrowser():

    @abstractmethod
    def find_all_children(self, name):
        pass


class Relationships(RelationshipBrowser):
    # low level module
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    # solution
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    # high level module
    # (old way)
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f"John has a child called {r[2].name}")

    # solution
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')

PARENT = Person('John')
CHILD1 = Person('Chris')
CHILD2 = Person('Matt')

RL = Relationships()
RL.add_parent_and_child(PARENT, CHILD1)
RL.add_parent_and_child(PARENT, CHILD2)

Research(RL)
