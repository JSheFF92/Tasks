def abbrev_name(name):
    d = name.split(" ")
    b = d[0][0].upper()
    c = d[1][0].upper()
    print(b+"."+c)
    return b+"."+c


if __name__ == "__main__":

    abbrev_name("jeka shevchuk")