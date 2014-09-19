#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

'''
分析思路：
20个格子从左上走到右下，即需要向右走20步，向下走20步，共40步。
考虑走的顺序是"rrrrrrrrrrrrrrrrrrrrdddddddddddddddddddd"为一种，
即求20个r和20个d的排列方法。由数学排列组合知识可知为C(40,20)*C(20,20)
'''
from helper import combination_numbers
print combination_numbers(40,20)