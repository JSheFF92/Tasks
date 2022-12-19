def square_digits(num):

    lst = str(num)
    b = ""
    for i in (lst):
         b += str(int(i)*int(i))
    d = "".join(b)
    print(int(d))

# return int(''.join(str(int(d)**2) for d in str(num)))

if __name__ == "__main__":
    square_digits(9119)