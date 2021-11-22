

from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):

    def connect_to(self, other):
        if self == other:
            return

        for x in self:
            for y in other:
                x.outputs.append(y)
                y.inputs.append(x)


class Neuron(Connectable):
    def __init__(self, name: str) -> None:
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self) -> str:
        return "{}, {} inputs, {} outputs.".format(self.name, len(self.inputs), len(self.outputs))

    def __iter__(self):
        # turn a scaler into a vector / array
        yield self


class NeuronLayer(Connectable, list):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name = name
        for index in range(count):
            self.append(Neuron('{}-{}'.format(self.name, index)))

    def __str__(self) -> str:
        return "{} with length of {} neurons.".format(self.name, len(self))


if __name__ == '__main__':
    neuron_one = Neuron("Neuron One")
    neuron_two = Neuron("Neuron Two")

    layer_one = NeuronLayer("Layer One", 3)
    layer_two = NeuronLayer("Layer Two", 5)

    neuron_one.connect_to(neuron_two)
    neuron_one.connect_to(layer_one)
    layer_one.connect_to(neuron_two)
    layer_one.connect_to(layer_two)

    print(neuron_one)
    print(neuron_two)
    print(layer_one)
    print(layer_two)
