"""
Flyweight
- A space optimization technique that lets us use less memory by
  storing externally the data associated with similar objects

Motivation
- Avoid redundancy when storing data
- E.g., MMORPG
  - Plenty of users with identical first/last names
  - No sense in storing same first/last name over and over again
  - Store a list of names and references to them
- E.g., bold or italic text formatting
  - Don't want each character to have a formatting character
  - Operate on ranges (e.g., line number, start/end positions)
"""

import string
import random


class User:
    def __init__(self, name):
        self.name = name


class User2:
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1
        self.names = [get_or_add(x) for x in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return ''.join(
        [random.choice(chars) for x in range(8)]
    )


if __name__ == "__main__":
    USERS = []

    FIRST_NAMES = [random_string() for x in range(10)]
    LAST_NAMES = [random_string() for x in range(10)]

    # naive
    # for first in FIRST_NAMES:
    #     for last in LAST_NAMES:
    #         USERS.append(User(f'{first} {last}'))

    # better
    for first in FIRST_NAMES:
        for last in LAST_NAMES:
            USERS.append(User2(f'{first} {last}'))

    for u in USERS:
        print(u)
        print(u.names)
    print(u.strings)
