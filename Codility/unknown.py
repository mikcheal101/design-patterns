# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys


def solution(A, B, K):
    # write your code in Python 3.6
    response = 0
    if A < B and B >= K:

        if A < K:
            starting_point = K
        else:
            if A % K == 0:
                starting_point = A
            else:
                starting_point = A + (K - (A % K))

        stopping_point = B - (B % K)
        response = (stopping_point / K) - (starting_point / K)
    return int(response + 1)

# 6, 8, 10,

# recieves A, B , K
# returns the number of intergers with the range A - B that are divisible by K


if __name__ == "__main__":
    # a = 6
    # b = 11
    # k = 2
    # a = 11
    # b = 345
    # k = 17
    # a = 0
    # b = 1
    # k = 11
    a = 0
    b = sys.maxsize
    k = sys.maxsize
    print(str(solution(a, b, k)))
