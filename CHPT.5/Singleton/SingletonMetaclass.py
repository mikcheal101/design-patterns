class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading Database')



if __name__ == "__main__":
    a = Database()
    b = Database()
    c = Database()
    print(a == b)