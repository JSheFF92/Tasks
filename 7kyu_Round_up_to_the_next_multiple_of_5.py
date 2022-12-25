def round_to_next5(n):

    while n % 5 != 0:
        n += 1
    print(n)

    # return n + (5 - n) % 5

if __name__ == "__main__":
    round_to_next5(-2)
