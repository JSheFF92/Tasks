def digitize(n):
    b = str(n)

    mass = []
    for i in b[::-1]:
        mass += i

    lstint = [int(x) for x in mass]

    print(lstint)

    # return map(int, str(n)[::-1])
    # return [int(x) for x in str(n)[::-1]]
if __name__ == "__main__":

    digitize(35231)