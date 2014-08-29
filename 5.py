# -*- coding: utf-8 –*-
__author__ = 'apple'
def gcd(m, n):
    '''
    :param m: int
    :param n: int
    :return: int
    求最大公因数
    >>> gcd(6, 8)
    2
    '''
    return m if n == 0 else gcd(n, m % n)

def lcm(m, n):
    '''
    :param m: int
    :param n: int
    :return: int
    求最小公倍数
    >>> lcm(6, 8)
    24
    '''
    return m * n // gcd(m, n)

def smallest_divided(num_list):
    '''
    :param num_list: list of int
    :return: int
    Find the smallest number that can be divided by each of the numbers in num_list
    >>> smallest_divided(range(1,11))
    2520
    '''
    assert len(num_list) >= 2
    num_list.sort(reverse = True)
    result = 1
    for i in num_list:
        if result % i != 0:
            result = lcm(result, i)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print smallest_divided(range(1, 21))