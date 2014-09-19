#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

from helper import divisorGen
NUM = 10000
# 返回除自己外的因数的和，若是质数， 则为1
sum_proper_divisors = lambda n:sum(divisorGen(n))-n

sum_proper_divisors_dic = {}
amicable_numbers = set()
for i in xrange(3, NUM+1):
	if i not in sum_proper_divisors_dic:
		sum_proper_divisors_dic[i] = sum_proper_divisors(i)
	pair = sum_proper_divisors_dic[i]
	if pair == 1 or pair == i:
		continue
	if pair not in sum_proper_divisors_dic:
		sum_proper_divisors_dic[pair] = sum_proper_divisors(pair)	
	if sum_proper_divisors_dic[pair] == i:
		print i, pair
		amicable_numbers.add(i)
		amicable_numbers.add(pair)

print sum(amicable_numbers)	