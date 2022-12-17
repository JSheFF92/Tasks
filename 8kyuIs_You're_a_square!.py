
def is_square(n):

    b = n ** 0.5

    if b * b == n:
        print("true")
    else:print("false")

if __name__ == "__main__":

    is_square(25)