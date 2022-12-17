def smash(words):
    b = ""
    for i in words:
        b += i+" "
    print("".join(b).rstrip())

    # print(" ".join(words))

if __name__ == '__main__':
    smash(["this", "is", "a", "really", "long", "sentence"])

