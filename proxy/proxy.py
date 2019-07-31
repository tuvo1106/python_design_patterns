"""
Proxy
- A class that functions as an interface to a particular resource.
  The resource can be remote, expensive to construct, or may
  require logging or some other added functionality

Motivation
- Same interface, entirely different behavior
- Types: logging, virtual,  guarding

Proxy vs Decorator
- Proxy provides identical inferface, decorator provides enhanced 
  interface
- Decorator typically aggregates (or has reference to) what it is
  decorating; proxy doesn't have to
- Proxy might not even be working with a materialized object
"""


class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car being driven by {self.driver.name}')


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self.car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self.car.drive()
        else:
            print('Driver too young')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    CAR = CarProxy(Driver('John', 19))
    CAR.drive()
