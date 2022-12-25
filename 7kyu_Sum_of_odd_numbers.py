def row_sum_odd_numbers(n):
    b = n * n

    c = (b + 1 - (n))* n + (b - n)

    print(c)
    k = n*n*n
    print(k)

if __name__ == "__main__":

    row_sum_odd_numbers(3)