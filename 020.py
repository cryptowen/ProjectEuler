#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

from helper import factorial
fac_100 = factorial(100)
print sum(int(i) for i in str(fac_100))