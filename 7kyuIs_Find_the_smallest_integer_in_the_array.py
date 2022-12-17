def find_smallest_int(numbers):

    g = numbers.split(" ")
    result = [int(item) for item in g]
    result.sort()
    d = str(result[-1]), str(result[-0])
    e = d[0]
    t = d[-1]
    g = e+" "+t
    print(g)




if __name__ == "__main__":
    find_smallest_int("8 3 -5 42 -1 0 0 -9 4 7 4 -4")