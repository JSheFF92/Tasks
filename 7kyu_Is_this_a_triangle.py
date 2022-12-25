def is_triangle(a, b, c):

        if a+b>c and b+c>a and a+c>b and a > 0 and b > 0 and c > 0:
            print("true")

        else:
            print("fa")


if __name__ == "__main__":

    is_triangle(6, -1, 0)