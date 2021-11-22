

class Calculation(list):
    def __init__(self, arr) -> None:
        self.array = arr

    def calculate(self):
        minimum = None
        index = None
        for i in range(0, len(self.array) - 1):
            result = 0
            if len(self.array) > i + 1:
                result = self.array[i] + self.array[i + 1]
            else:
                result = self.array[i]
            if minimum:
                if minimum > result:
                    index = i   
                    minimum = result 
            else:
                index = i
                minimum = result

            self.append(result)
        return index


def solution(A):
    # write your code in Python 3.6
    calc = Calculation(A)
    return calc.calculate()


if __name__ == "__main__":
    array = [4, 2, 2, 5, 1, 5, 8]
    print(str(solution(array)))
