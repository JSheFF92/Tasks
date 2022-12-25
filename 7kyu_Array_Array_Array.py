from curses.ascii import isdigit

from curses.ascii import isdigit


def explode(arr):

    # h = []
    #
    # if isdigit(str(arr[0])) == False and isdigit(str(arr[1])) == True:
    #     for b in range(arr[1]):
    #         h.append(arr)
    #     print(h)
    # elif isdigit(str(arr[0])) == True and isdigit(str(arr[1])) == False:
    #     for l in range(arr[0]):
    #         h.append(arr)
    #     print(h)
    # elif isdigit(str(arr[0])) == False and isdigit(str(arr[1])) == False:
    #     print("Void!")
    # if isdigit(str(arr[0])) == True and isdigit(str(arr[1])) == True:
    #     g = int(arr[0]) + int(arr[1])
    #     for i in range(g):
    #         h.append(arr)
    #     print(h)

    if type(arr[0]) != int and type(arr[1]) != int:
        print("Void!")
    elif type(arr[0]) == int and type(arr[1]) != int:
        print([arr] * arr[0])
    elif type(arr[0]) != int and type(arr[1]) == int:
        print([arr] * arr[1])
    else:
        print([arr] * sum(arr))


if __name__ == "__main__":
    explode([3, "a"])
