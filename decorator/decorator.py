"""
Decorator
- Facilitates the addition of behaviors to individual objects without
  inheriting from them

Motivation
- Want to augment an object with additional functionality
- Do no want to rewrite or alter existing code (OCP)
- Want to keep new functionality separate (SRP)
- Need to be able to interact with existing structures
- Two options:
  - Inherit from required object (if possible)
  - Build a Decorator, which simply references the decorated object(s)
"""

import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int(end - start) * 1000} ms')
        return result
    return wrapper


@time_it
def some_op():
    print('Starting op')
    time.sleep(1)
    print('We are done')
    return 123

# some_op()
# time_it(some_op)
some_op()
