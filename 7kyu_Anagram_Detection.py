def is_anagram(test, original):

    a = test.lower()
    b = original.lower()
    later1 = []
    later2 = []

    for i in a:
        later1.append(i)

    for j in b:
        later2.append(j)

    print(sorted(later1) == sorted(later2))





if __name__ == "__main__":
    is_anagram("dumble", "bumble")