# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    placeholder=0
    score=0
    
    for _, value in enumerate(A):
        if value == 0:
            placeholder += 1
        else:
            score += placeholder

    return score if score <= 10 ** 9 else -1


if __name__ == "__main__":
    a = [0, 1, 0, 1, 1]

    print(str(solution(a)))

