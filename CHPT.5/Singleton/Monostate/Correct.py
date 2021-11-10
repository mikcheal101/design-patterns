class MonoState:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(MonoState, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class CFO(MonoState):
    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.money_managed = 0.0

    def __str__(self):
        return "{} manages {}".format(self.name, self.money_managed)


if __name__ == "__main__":
    a = CFO()
    a.name = "Segun Oba"
    a.money_managed = 210000

    b = CFO()
    b.name = "Ruth Ogah"
    b.money_managed = 89220

    print(a)
    print(10 * "")
    print(b)
