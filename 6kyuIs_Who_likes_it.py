def likes(names):

    count = 0
    b =0
    for i in names:
        count +=1
        b +=1
    print(count)
    c = count - 2

    if count == 1:
        print(f'{names[0]} likes this')
    elif count == 2:
        print(f'{names[0]} and {names[1]} like this')
    elif count == 3:
        print(f'{names[0]}, {names[1]} and {names[2]} like this')
    elif count >= 2:
        print(f'{names[0]}, {names[1]} and {len(names)-2} others like this')
    else:
        print('no one likes this')



if __name__ == "__main__":

    likes(['Alex', 'Jacob', 'Mark', 'Max','Alex', 'Jacob', 'Mark', 'Max'])