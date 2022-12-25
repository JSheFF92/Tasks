import operator
from collections import Counter, defaultdict
from itertools import count


def find_it(seq):
    d = {}
    for i in seq:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    inv = [k for k, v in d.items()
           if v % 2 == 1]

    print(inv[0])

# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i

if __name__ == '__main__':
    find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])

# Дан массив целых чисел, найдите то, которое встречается нечетное количество раз.
#
# Всегда будет только одно целое число, которое встречается нечетное количество раз.
# @test.it("find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) should return 5 (because it appears 3 times)")
# def _():
#     test.assert_equals(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)

#
# @test.it("find_it([1,1,2,-2,5,2,4,4,-1,-2,5]) should return -1 (because it appears 1 time)")
# def _():
#     test.assert_equals(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1);
#
#
# @test.it("find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]) should return 5 (because it appears 3 times)")
# def _():
#     test.assert_equals(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5);
#
#
# @test.it("find_it([10]) should return 10 (because it appears 1 time)")
# def _():
#     test.assert_equals(find_it([10]), 10);
#
#
# @test.it("find_it([10, 10, 10]) should return 10 (because it appears 3 times)")
# def _():
#     test.assert_equals(find_it([10, 10, 10]), 10);

#
# @test.it("find_it([1,1,1,1,1,1,10,1,1,1,1]) should return 10 (because it appears 1 time)")
# def _():
#     test.assert_equals(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10);
#
#
# @test.it("find_it([5,4,3,2,1,5,4,3,2,10,10]) should return 1 (because it appears 1 time)")
# def _():
#     test.assert_equals(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1);
