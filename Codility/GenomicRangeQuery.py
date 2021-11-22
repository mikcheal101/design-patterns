

def solution(S, P, Q):
    # write your code in Python 3.6

    keys = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    temp = [keys[i] for i in S]
    sub_string = [min(temp[P[index]: Q[index] + 1]) for index in range(len(P))]
    return sub_string


if __name__ == "__main__":
    s = list("CAGCCTA")
    p = [2, 5, 0]
    q = [4, 5, 6]
    print(str(solution(s, p, q)))
