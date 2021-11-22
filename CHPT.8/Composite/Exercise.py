from abc import ABC
from collections.abc import Iterable


class Connectable(ABC, Iterable):
    @property
    def sum(self) -> int:
        """ method of an abstract class """
        return 0


class SingleValue(Connectable):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self

    @property
    def sum(self) -> int:
        sum_value = 0
        for i in self:
            sum_value += i.value
        return sum_value 


class ManyValues(list, Connectable):
    @property
    def sum(self) -> int:
        value = 0
        for i in self:
            value += 1 if isinstance(i, int) else i.sum()
        return value


if __name__ == '__main__':
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)

    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)

    # for i in single_value:
    #     print('single value: {}'.format(i))

    # for i in other_values:
    #     print('other values: {}'.format(i))

    # for i in all_values:
    #     print('all values: {}'.format(i))

    # print(all_values.sum())
    # print(all_values.sum() == 66)



