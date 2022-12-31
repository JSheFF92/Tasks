def gimme(mass):

    d = mass.copy()
    d.sort()
    oklist = []

    for i in d:
        oklist.append(i)
    ok = oklist[1]
    print(mass.index(ok))


    # return inputArray.index(sorted(inputArray)[1])

if __name__ == "__main__":

    gimme([2, 3, 1])