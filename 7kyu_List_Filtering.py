from curses.ascii import isdigit
from unicodedata import digit


def filter_list(l):
    gr = [i for i in l if type(i) == int]
    print(gr)


if __name__ == "__main__":
    filter_list([1, 2, 'aasf', '1', '123', 123])
