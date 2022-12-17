import math

def nb_year(p0, percent, aug, p):

    count = 0
    while p0 < p:
        g = p0 + (p0 * (percent / 100)) + aug
        p0 = math.floor(g)
        count += 1
    print(count)

if __name__ == "__main__":

    nb_year(1500, 5, 100, 5000)