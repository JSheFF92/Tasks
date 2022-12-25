from curses.ascii import isdigit
from unicodedata import digit


def number(bus_stops):
    # g = []
    # for i in bus_stops:
    #     g.append((i[0]-sum(i[1:])))
    # print(sum(g))

    print(sum([stop[0] - stop[1] for stop in bus_stops]))


if __name__ == "__main__":
    number([[10, 0], [3, 5], [5, 8]])
