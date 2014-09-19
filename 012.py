# -*- coding: utf-8 –*-
__author__ = 'apple'

from helper import next_prime, list_product

prime_list = [2]
for i in xrange(9):
    next_prime(prime_list)

print prime_list
print list_product(prime_list)
'''
质因数个数   至多因数个数      排列
1   2   1+1
2   4   1+2+1
3   8   1+3+3+1
4   16  1+4+6+4+1
5   32
6   64
7   128
8   256
9   512

    500
因此至多9个不同的质因数就可以有超过500个因数，因此质因数个数在9个以内，质数不用求太多
'''
def fjzys(num):
    '''
    :param num: int
    :return: list of divisor
    分解质因数
    '''
    pass


# method 1: simplest and most slow
# def num_of_divisors(n):
#     return sum( 1 for i in xrange(1, n+1) if n%i==0 )
#
# num = 0
# import itertools
# for i in itertools.count(1):
#     num += i
#     n_o_d = num_of_divisors(num)
#     print num, n_o_d
#     if n_o_d == 500:
#         # print num
#         break
