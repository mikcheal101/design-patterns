

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    result_space = 0
    try:

        temp_result_space = dict()
        for i in A:
            if i in temp_result_space:
                temp_result_space[i] += 1
            else:
                temp_result_space[i] = 1
        result_space = min(temp_result_space, key=temp_result_space.get)
    except:
        pass
    
    return result_space

if __name__ == "__main__":
    numbers = [9, 3, 9, 3, 9, 7, 9 ]
    # numbers = [42]
    print(solution(numbers))
