# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def shift_right(array):
    array_len = len(array)
    new_array = [None] * array_len
    for i in range(array_len):
        print("swapping: ({} <=> {})".format(i, (i + 1) % array_len))
        new_array[(i + 1) % array_len] = array[i]
    return new_array

def solution(A, K):
    # write your code in Python 3.6
    for _ in range(K):
        A = shift_right(A)
    return A


if __name__ == "__main__":
    # array = [3, 8, 9, 7, 6]
    # k = 3

    # array = [0] * 3
    # k = 1

    array = [1, 2, 3, 4]
    k = 4
    print(solution(array, k))