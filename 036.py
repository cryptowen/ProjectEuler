#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

from helper import is_palindromic

MAX_NUM = 10**6

# palindromic_list = []
# for i in xrange(1, MAX_NUM+1):
# 	if is_palindromic(str(i)) and is_palindromic(bin(i)[2:]):
# 		palindromic_list.append(i)

# print sum(palindromic_list)

print sum(i for i in xrange(1, MAX_NUM+1) if is_palindromic(str(i)) and is_palindromic(bin(i)[2:]))