def reverse_words(str):
    print(' '.join(s[::-1] for s in str.split(' ')))


    # b = []
    # for i in str[::-1].split(" "):
    #     b.append(i)
    # b.reverse()
    # return ' '.join((b))


if __name__ == "__main__":
    reverse_words("sihT si na !elpmaxe")
