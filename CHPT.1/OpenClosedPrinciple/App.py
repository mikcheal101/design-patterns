from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product
    
    def filter_by_size(self, products, size):
        for product in products:
            if product.size == size:
                yield product

    # this approach is causing "a state space explosion."
    def filter_by_size_color(self, products, size, color):
        for product in products:
            if product.size == size and product.color == color:
                yield product

# Specification pattern

class Specification:
    def is_satisfied(self, item):
        pass

class Filter:
    def filter(self, items, specification):
        pass

class ColorSpecification(Specification):

    def __init__(self, color):
        super().__init__()
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):

    def __init__(self, size):
        super().__init__()
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):

    def __init__(self, *args):
        super().__init__()
        self.args = args

    def is_satisfied(self, item):
        return all(map( lambda spec: spec.is_satisfied(item), self.args ))

class OrSpecification(Specification):

    def __init__(self, *args):
        super().__init__()
        self.args = args

    def is_satisfied(self, item):
        return any(map( lambda spec: spec.is_satisfied(item), self.args ))

class ColorOrSizeSpecification(Specification):
    
    def __init__(self, color=None, size=None):
        super().__init__()
        self.size = size
        self.color = color

    def is_satisfied(self, item):
        if self.size or self.color:
            return self.color == item.color or self.size == item.size
        return False

class BetterFilter(Filter):
    def filter(self, items, specification):
        for item in items:
            if specification.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]
    
    pf = ProductFilter()
    print("Green Products (old way): ")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is Green!")


    bf = BetterFilter()
    print("Green Products (new way): ")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} is Green!")


    # large products
    print('Large Products: ')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is Large!")

    # large or green products
    print('Green or Large Products (incorrect): ')
    green_or_large = ColorOrSizeSpecification(color=Color.GREEN, size=Size.LARGE)
    for p in bf.filter(products, green_or_large):
        print(f" - {p.name} is green or Large!")

    print('Blue and Large Products (correct): ')
    blue_and_large = AndSpecification(large, ColorSpecification(color=Color.BLUE))
    for p in bf.filter(products, blue_and_large):
        print(f" - {p.name} is blue and Large!")
