from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    # def connect_to(self, other):
    #     self.outputs.append(other)
    #     other.inputs.append(self)

    def __iter__(self):
        yield self

    def __str__(self):
        return f'{self.name}, {len(self.inputs)} inputs, +\
                {len(self.outputs)} outputs'


class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f'{name}-{x}'))

    def __str__(self):
        return f'{self.name} with {len(self)} neurons'


def connect_to(self, other):
    if self == other:
        return

    for s in self:
        for o in other:
            s.outputs.append(o)
            o.inputs.append(s)


NEURON1 = Neuron('n1')
NEURON2 = Neuron('n2')
LAYER1 = NeuronLayer('L1', 3)
LAYER2 = NeuronLayer('L2', 4)

# Neuron.connect_to = connect_to
# NeuronLayer.connect_to = connect_to

NEURON1.connect_to(NEURON2)
NEURON1.connect_to(LAYER1)
LAYER1.connect_to(NEURON2)
LAYER1.connect_to(LAYER2)

print(NEURON1)
print(NEURON2)
print(LAYER1)
print(LAYER2)
