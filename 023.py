#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

from helper import proper_divisors
NUMBER_TYPE = {
	0: 'perfect_number',	# proper_divisors_sum(n) == n
	1: 'abundant number',	# proper_divisors_sum(n) > n
	-1: 'deficient_number',	# proper_divisors_sum(n) < n
}

MAX = 28123
is_abundant = lambda n: sum(proper_divisors(n)) > n
# for i in xrange(2, MAX+1):
# 	print i, ':', is_abundant(i)

abundant_numbers = filter(is_abundant, range(2,MAX))
# for i in xrange(12, MAX+1):
# 	for abundant in abundant_numbers:
# 		if i > abundant and is_abundant(i-abundant):
# 			return 
sums = 0
for i in range(12, MAX+1):
    for abundant in abundant_numbers:
        if abundant >= i and is_abundant(i + abundant):
            sums += i
print(sums)			