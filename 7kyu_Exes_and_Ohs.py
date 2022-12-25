def xo(s):
    num = 0
    num2 = 0

    low = s.lower()

    for i in low:
        if i == 'x':
            num += 1
        elif i == 'o':
            num2 += 1

    print(num==num2)


if __name__ == "__main__":
    xo('xxxoo')