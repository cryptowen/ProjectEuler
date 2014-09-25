#!/usr/bin/env python
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'
from primes import primes
circular_primes = []
MAX_NUM = 1000
# rotate = lambda n:[int(''.join(k)) for k in itertools.permutations([i for i in str(n)])]


def rotate(n):
    """
    >>> rotate(179)
    [179, 791, 917]
    """
    s = str(n)
    assert '0' not in s
    result = []
    for i in xrange(len(s)):
        result.append(int(s[i:] + s[:i]))

    return result


def is_circular(n):
    """ 返回n是不是circular prime
    >>> is_circular(197)
    True
    >>> is_circular(9)
    False
    >>> is_circular(1)
    False
    >>> is_circular(98)
    False
    """
    return all(i in primes for i in rotate(n))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    for i in xrange(1, MAX_NUM + 1):
        if ('0' in str(i)) or (i in circular_primes):
            continue
        if is_circular(i):
            circular_primes.extend(rotate(i))
    print len(circular_primes)
