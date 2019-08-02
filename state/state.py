"""
State
- A pattern in which the object's behavior is determined by its state. An
  object transitions from one state to another (something needs to trigger
  a transition).
- A formalized construct which manages state and transitions is called a state
  machine.
Motivation
- Consider an ordinary telephone
- What you do with it depends on the state of the phone/line
  - If it's ringing or you want to make a call, you can pick it up
  - Phone must be off the hook to talk/make a call
  - If you try calling someone, and it's busy, you put the handset down
- Change in state can be explicit or in response to an event (Observer pattern)
"""


# interesting but not practical :)
from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def on(self, switch):
        print('Light is already on')

    def off(self, switch):
        print('Light is already off')


class OnState(State):
    def __init__(self):
        print('Light turned on')

    def off(self, switch):
        print('Turning light off...')
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print('Light turned off')

    def on(self, switch):
        print('Turning light on...')
        switch.state = OnState()


if __name__ == '__main__':
    SW = Switch()

    SW.on()
    SW.off()
    SW.off()
