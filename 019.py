#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

'''
python的calendar模块提供了查询周几的方法，如
calendar.weekday(2014, 9, 17)
将返回2，表示星期三（0表示周一）
'''

import calendar
sunday_num = 0
for year in xrange(1901, 2001):
	for month in xrange(1, 13):
		if calendar.weekday(year, month, 1) == 6:
			sunday_num += 1

print sunday_num			