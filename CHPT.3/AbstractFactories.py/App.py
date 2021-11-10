from abc import ABC
from enum import Enum, auto

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious")

class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious")

class IHotDrinkFactory(ABC):
    # abstract class/ interface
    def prepare(self, amount):
        pass

class TeaFactory(IHotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water pour {amount} ml, enjoy!")
        return Tea()

class CoffeeFactory(IHotDrinkFactory):
    def prepare(self, amount):
        print(f"Put some beans, boil water pour {amount} ml, enjoy!")
        return Coffee()

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    is_initialized = False

    def __init__(self) -> None:
        if not self.is_initialized:
            self.is_initialized = True
            for i in self.AvailableDrink:
                name = f"{i.name[0]}{i.name[1:].lower()}"
                factory_name = f"{name}Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Available Drinks:")
        counter = 0
        for name, instance in self.factories:
            print(f"\t [{counter}] {name}")
            counter += 1
        s = input(f"Please pick drink (0 - {len(self.factories) - 1}): ")
        index = int(s)
        s = input(f"Specify Amount: ")
        amount = int(s)

        return self.factories[index][1].prepare(amount)


def make_drink(type):
    if type == "tea":
        return TeaFactory().prepare(200)
    elif type == "coffee":
        return CoffeeFactory().prepare(50)
    else:
        return None

if __name__ == "__main__":
    # entry = input("What kind of drink would you like? ")
    # drink = make_drink(entry)
    # if drink:
    #     drink.consume()

    hdm = HotDrinkMachine()
    hdm.make_drink()