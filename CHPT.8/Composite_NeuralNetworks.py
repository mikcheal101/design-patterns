class Neuron:
    def __init__(self, name: str) -> None:
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self) -> str:
        return "{}, {} inputs, {} outputs.".format(self.name, len(self.inputs), len(self.outputs))

    def connect_to(self, other):
        self.outputs.append(other)
        other.inputs.append(self)


class NeuronLayer(list):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name = name
        for index in range(count):
            self.append(Neuron('{}-{}'.format(self.name, index)))

    def __str__(self) -> str:
        return "{} with length of {} neurons.".format(self.name, len(self))


def connect_to(parent, child):
    if parent == child:
        return

    for x in parent:
        for y in child:
            x.outputs.append(y)
            y.inputs.append(x)


if __name__ == '__main__':
    neuron_one = Neuron("Neuron One")
    neuron_two = Neuron("Neuron Two")

    layer_one = NeuronLayer("Layer One", 3)
    layer_two = NeuronLayer("Layer Two", 5)

    neuron_one.connect_to(neuron_two)
    neuron_one.connect_to(layer_one)
    layer_one.connect_to(neuron_two)
    layer_one.connect_to(layer_two)
