def remove_smallest(numbers):

    b = numbers.copy()

    if b == numbers[0]:
        print(numbers)

    b.remove(min(b))
    print(b)


if __name__ == "__main__":
    remove_smallest([122, 299, 253, 174, 362])