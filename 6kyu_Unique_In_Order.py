
def unique_in_order(iterable):
    a = list(iterable)

    g = []
    for i in range(0, len(a)):
        if a[i] != a[i-1] or i == 0:
                g.append(a[i])

    print(g)


if __name__ == "__main__":
    unique_in_order(['A'])