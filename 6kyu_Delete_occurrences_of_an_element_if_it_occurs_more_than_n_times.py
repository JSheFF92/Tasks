from collections import Counter

def delete_nth(order,max_e):
    mass = order.copy()
    end = []
    for number, count in (Counter(mass).items(), ):
        if count > max_e:
            mass.remove(number)
    print(mass)
        # if count > max_e:
        #     for j in range(max_e):
        #         end.append(number)
        #     continue
        # else:
        #     for i in range(count):
        #         end.append(number)
    print(end)




if __name__ == "__main__":

    delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3)
                # [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5]
                # [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]