def find_short(s):

    d = [i for i in s.split(" ")]

    o = []
    for i in d:
        b = int(len(i))
        o.append(b)
    print(min(o))


if __name__ == "__main__":

    find_short("bitcoin take over the world maybe who knows perhaps")