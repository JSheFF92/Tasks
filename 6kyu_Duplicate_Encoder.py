def duplicate_encode(word):

    lowerr = word.lower()

    print("".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()]))

    b = ""
    for i in lowerr:
        if lowerr.count(i) > 1:
            b += ")"
        elif lowerr.count(i) == 1:
            b += '('
        else:
            b += ")"
    print(b)

if __name__ == "__main__":
    duplicate_encode("Success")