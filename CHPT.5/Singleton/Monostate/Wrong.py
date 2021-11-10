class CEO:
    __shared_state = {
        'name': 'Steve',
        'age': 55,
    }

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return "{} is {} years old!".format(self.name, self.age)


if __name__ == "__main__":
    ceo_one = CEO()
    ceo_two = CEO()
    ceo_two.age = 88

    print(ceo_one)
    print(ceo_two)