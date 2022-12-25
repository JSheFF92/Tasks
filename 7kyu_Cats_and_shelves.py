import math


def solution(start, finish):
        print(math.floor((finish-start)/3) + (finish-start)%3)


if __name__ == "__main__":
    solution(1,5)