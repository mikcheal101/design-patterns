
# decorator definition
def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance

@singleton
class Database:
    def __init__(self) -> None:
        print("Loading Database")


if __name__ == "__main__":
    a = Database()
    b = Database()
    c = Database()
    print(a == b)