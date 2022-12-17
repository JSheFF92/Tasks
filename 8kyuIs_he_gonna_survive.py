def hero(bullets, dragons):

    if dragons >= bullets:
        print(False)

    elif bullets >= dragons and ((bullets * dragons) % 2 == 0 and (bullets * dragons) % 2 == 1):
        print(True)




    return

if __name__ == "__main__":

    hero(6, 2)