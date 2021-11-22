# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # write your code in Python 3.6
    
    # get the binary for N
    binary_string = format(N, 'b')
    previous_number = None
    maximum_number = None

    for index, binary_character in enumerate(binary_string):
        try:
            binary_number = int(binary_character)
            if binary_number == 1:
                if previous_number == None and maximum_number == None:
                    maximum_number = 0
                else:
                    score = index - 1
                    score -= previous_number
                    maximum_number = maximum_number if maximum_number > score else score
                
                previous_number = index
        except Exception as e:
            print(e)

    return maximum_number



if __name__ == "__main__":
    n = 32
    print("[i] Solution: {}".format(solution(n)))
