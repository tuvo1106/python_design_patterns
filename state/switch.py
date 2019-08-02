from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


if __name__ == '__main__':
    CODE = '1234'
    STATE = State.LOCKED
    ENTRY = ''

    while True:
        if STATE == State.LOCKED:
            ENTRY += input(ENTRY)

            if ENTRY == CODE:
                STATE = State.UNLOCKED

            if not CODE.startswith(ENTRY):
                # the CODE is wrong
                STATE = State.FAILED
        elif STATE == State.FAILED:
            print('\nFAILED')
            ENTRY = ''
            STATE = State.LOCKED
        elif STATE == State.UNLOCKED:
            print('\nUNLOCKED')
            break
