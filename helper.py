#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

import math

def div_frac(a, b=1):
    """ 返回b/a的循环小数表示形式
    >>> div_frac(2)
    0.5
    >>> div_frac(3)
    0.(3)
    >>> div_frac(7)
    0.(142857)
    """
    

def fib():
    """ 返回fibonacci数列
    >>> a = fib()
    >>> for i in range(6):
    ...     print a.next()
    1
    1
    2
    3
    5
    8
    >>> b = fib()
    >>> list(b.next() for i in range(9))
    [1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a+b

def proper_divisors(n):
    """ 返回n除自己外的因数列表
    >>> proper_divisors(100)
    [1, 2, 4, 5, 10, 20, 25, 50]
    """
    proper_divisors_list = list(divisorGen(n))
    proper_divisors_list.pop()
    return proper_divisors_list

def divisorGen(n):
    """ 返回n的所有因数, n > 1
    >>> for i in divisorGen(100):
    ...     print i
    1
    2
    4
    5
    10
    20
    25
    50
    100
    >>> list(divisorGen(100))
    [1, 2, 4, 5, 10, 20, 25, 50, 100]
    """
    assert n > 1
    factors = primes_divisor_dic(n)
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def rwh_primes2(n = 10**6):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def primes_divisor_list(n):
    """ 返回n以内的所有质因数，以列表显示

    >>> primes_divisor_list(100)
    [2, 2, 5, 5]
    >>> primes_divisor_list(18)
    [2, 3, 3]
    >>> primes_divisor_list(220)
    [2, 2, 5, 11]
    """
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def primes_divisor_dic(n):
    """ 返回n以内的所有质因数，以因数对显示

    >>> primes_divisor_dic(100)
    [(2, 2), (5, 2)]
    >>> primes_divisor_dic(18)
    [(2, 1), (3, 2)]
    >>> primes_divisor_dic(220)
    [(2, 2), (11, 1), (5, 1)]
    """
    from collections import defaultdict
    primfac_dic = defaultdict(int)
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac_dic[d] += 1  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac_dic[n] += 1
    return list(primfac_dic.items())

def next_prime(prime_list):
    last_prime = prime_list[-1]
    while True:
        last_prime += 1
        is_prime = True
        for prime in prime_list:
            if last_prime % prime == 0:
                is_prime = False
                break
            if prime > math.sqrt(last_prime):   # sqrt is faster than last_prime/2
                break
        if is_prime:
            # print last_prime
            prime_list.append(last_prime)
            return prime_list

list_product = lambda l: reduce(lambda x,y:int(x)*int(y), l)        

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000L
    >>> factorial(30L)
    265252859812191058636308480000000L
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000L

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

def permutation_numbers(a, b):    
    """ 实现排列算法，返回从a个数中取出b个进行排列（顺序有关）的方法数量

    >>> permutation_numbers(3, 2)
    6
    >>> permutation_numbers(5, 3)
    60
    """  
    assert a >= b >= 1
    return factorial(a) / factorial(a-b)

def combination_numbers(a, b):
    """ 实现组合算法，返回从a个数中取出b个（顺序无关）的方法数量

    >>> combination_numbers(3, 2)
    3
    >>> combination_numbers(3, 1)
    3
    """
    assert a >= b >= 1
    return factorial(a) / factorial(b) / factorial(a-b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()