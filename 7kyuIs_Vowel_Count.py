def get_count(sentence):

    count = 0

    for i in (sentence):
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count += 1
    print(count)


if __name__ == "__main__":

    get_count("")