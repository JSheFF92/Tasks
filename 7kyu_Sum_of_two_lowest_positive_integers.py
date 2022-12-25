def sum_two_smallest_numbers(numbers):

    numbers.sort()
    print(numbers[0] + numbers[1])

if __name__ == "__main__":
    sum_two_smallest_numbers([19, 5, 42, 2, 77])