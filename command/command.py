"""
Command
- An object which represents an instruction to perform a particular action.
  Contains all the information necessary for the action to be taken.

Motivation
- Ordinary statements are perishable
- Cannot undo member assignment
- Cannot directly serialize a sequence of actions (calls)
- Want an object that represents an operation
  - person should change its age to value 22
  - car should do explode()
- Uses: GUI commands , multilevel undo/redo, macro recording and more!
"""


from abc import ABC
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, balance = {self.balance}')

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, balance = {self.balance}')
            return True
        return False

    def __str__(self):
        return f'Balance = {self.balance}'


# optional
class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    def __init__(self, account, action, amount):
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None

    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        # strictly speaking this is not correct
        # (you don't undo a deposit by withdrawing)
        # but it works for this demo, so...
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == '__main__':
    BA = BankAccount()
    CMD = BankAccountCommand(BA, BankAccountCommand.Action.DEPOSIT, 100)
    CMD.invoke()
    print('After $100 deposit:', BA)

    CMD.undo()
    print('$100 deposit undone:', BA)

    ILLEGAL_CMD = BankAccountCommand(BA,
                                     BankAccountCommand.Action.WITHDRAW, 1000)
    ILLEGAL_CMD.invoke()
    print('After impossible withdrawal:', BA)
    ILLEGAL_CMD.undo()
    print('After undo:', BA)
