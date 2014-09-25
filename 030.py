#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

DIGITAL = 5

is_sum_of_power = lambda num, power: num == sum([ int(s) ** power for s in str(num)])
assert is_sum_of_power(1634, 4)

result = [i for i in xrange(2, 10**(DIGITAL+1)) if is_sum_of_power(i, DIGITAL)]
print result
print sum(result)

