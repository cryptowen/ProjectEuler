#!/usr/bin/env python     
# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

class Test(object):
    """docstring for Test"""
    def __init__(self):
        self.arg = 'hello'

    def printarg(self):
        print self.arg

if __name__ == '__main__':
    t = Test()
    t.printarg()        
        