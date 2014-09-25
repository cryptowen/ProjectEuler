#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

DIG = 10**10
result = 0
for i in xrange(1, 1000+1):
	result = result + i**i % DIG

print result % DIG