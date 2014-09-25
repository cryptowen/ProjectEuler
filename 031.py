#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
SUM = 200

def coin_sort(sum_coin, coin_list):
	""" 输入硬币列表和要得到的总合，输出可以拼出的个数

	>>> coin_sort(100, [1])
	1
	>>> coin_sort(100, [3])
	0
	>>> coin_sort(5, [1, 2])
	3
	>>> coin_sort(10, [1, 2, 5])
	10
	"""
	coin_list.sort()
	assert 0 not in coin_list
	assert sum_coin >= 0
	if len(coin_list) == 1:
		if sum_coin % coin_list[-1] == 0:
			return 1
		else:
			return 0
	else:
		max_last = sum_coin / coin_list[-1]
		result = 0
		for i in xrange(max_last+1):
			result += coin_sort(sum_coin-i*coin_list[-1], coin_list[:-1])
		return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()			
    print coin_sort(SUM, coin_list)

