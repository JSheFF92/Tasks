def lovefunc(flower1, flower2):
    if flower1 % 2 == 1 and flower2 % 2 == 0 or flower1 % 2 == 0 and flower2 % 2 == 1:
        print(True)
        return True
    else:
        print(False)
        return False

# Альтернатива
# def lovefunc(flower1, flower2):
#     return (flower1 + flower2) % 2

if __name__ == "__main__":

    lovefunc(2, 2)