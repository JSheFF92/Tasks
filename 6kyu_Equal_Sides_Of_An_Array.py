def find_even_index(arr):

    b = arr.copy()
# print(b)
# arr.reverse()
#
# print(arr)

    # l = 0

    # for h, numberleft in enumerate(b):
    #     l += numberleft
    #     k = 0
    #     for numberright in ((b[::-1])):
    #             # if b[i] + b[i + 1] - b[j] + b[j - 1] == 0:
    #         k += numberright
    #         if l-k == 0:
    #                     break
    #
    #     print(l, h)
    # print(l)l
        # break

    k = 0
    l = 0
    while True:

        for h, numberleft in enumerate(b):
            l += numberleft
            if l - k == 0:
                print(l)
                break


        for numberright in ((b[::-1])):
            # if b[i] + b[i + 1] - b[j] + b[j - 1] == 0:
            k += numberright

        if l-k == 0:
            print(l,k)


if __name__ == '__main__':
    find_even_index([14, 2, 3, 2, 11])
