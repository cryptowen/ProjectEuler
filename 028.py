#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

"""
1 	: 	1
3 	:	1,(3, 5, 7, 9)	#递增2
5	:	1, (3, 5, 7, 9), (13, 17, 21, 25)	#递增4
……
"""

average_diagonals, sum, delta, i = 1, 1, 5, 1
while True:
	i += 2
	average_diagonals += delta
	sum += average_diagonals*4
	if i >= 1001: 
		print sum
		break
	delta += 8

