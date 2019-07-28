"""
Singleton
- A component which is instantiated only once

Motivation
- For some components it only makes sense to have one in the system
  - Database repository
  - Object factory
- E.g., the initializer call is expensive
  - We only do it once
  - We provide everyone with the same instance
- Want to prevent anyone from creating additional copies
- Need to take care of lazy instantiation
"""
import random

class Database:

    _instance = None

    def __init__(self):
        id = random.randint(1, 101)
        print('Loading database from file')
        print(f'id = {id}')

    # redefine allocator
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
            .__new__(cls, *args, **kwargs)
        return cls._instance

d1 = Database()
d2 = Database()

print(d1 == d2)

# approach is not good enough, initializer still gets called
