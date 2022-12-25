def next_pal(val):
    g = 0 + val

    while True:
        g += 1
        b = str(g)
        if b[::-1] == b:
            return g


if __name__ == "__main__":
    next_pal(11)