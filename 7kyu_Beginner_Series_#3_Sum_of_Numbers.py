def get_sum(a,b):

    count = 0

    if b < a:
        for j in range(b, a - 1):
            count += j

    elif b == a or a == b:
        print (a)

    else:
        for i in range(a, b + 1):
            count += i

    print(count)


if __name__ == "__main__":
    get_sum(17, 17)