# not a reccommended approach


class CEO:
    __shared_state = {
        'name': 'Steve',
        'age': 55
    }

    def __init__(self):
        self.name = None
        self.age = None
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old'


CEO1 = CEO()
print(CEO1)

CEO2 = CEO()
CEO2.age = 77
print(CEO1)
print(CEO2)


class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} manages ${self.money_managed}'

CFO1 = CFO()
CFO1.name = 'Sheryl'
CFO1.money_managed = 1000
print(CFO1)

CFO2 = CFO()
CFO2.name = 'Ruth'
CFO2.money_managed = 2000

print(CFO1, CFO2, sep='\n')
