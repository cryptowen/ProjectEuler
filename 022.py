#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

# http://stackoverflow.com/questions/19068987/project-euler-22-off-by-18-609

from string import ascii_uppercase
name_score = lambda s:sum(ascii_uppercase.index(c)+1 for c in s)
with open('p022_names.txt', 'r') as f:
	names_str = f.read()
	names = sorted([name.strip('"') for name in names_str.split(',')])

print sum(name_score(name)*(names.index(name)+1) for name in names)