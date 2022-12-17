def disemvowel(string_):

    count = ''

    for i in (string_):
        if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i == "u" or i == "O" or i == "U":
            continue
        count +=i
    print(count)


if __name__ == "__main__":

    disemvowel("No offense but,Your writing is among the worst I've ever read")