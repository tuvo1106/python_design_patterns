"""
Observer
- An observer is an object that wishes to be informed about events happening
  in the system. The entity generating the event is an observable.
Motivation
- We need to be informed when certain things happen
  - Object's property changes
  - Object does something
  - Some external event
- We want to listen to events and be notified when they occur
  - Notification should include useful data
- Want to unsubscribe from events if we're no longer interested
"""


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'A doctor has been called to {address}')

if __name__ == '__main__':
    PERSON = Person('Sherlock', '221B Baker St')
    PERSON.falls_ill.append(lambda name, addr: print(f'{name} is ill'))
    PERSON.falls_ill.append(call_doctor)
    PERSON.catch_a_cold()

    # and you can remove subscriptions too
    PERSON.falls_ill.remove(call_doctor)
    PERSON.catch_a_cold()
