#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

from helper import fib
f = fib()
term = 0
while True:
	f_n = f.next()
	term += 1
	if len(str(f_n)) >= 1000:
		print term
		break