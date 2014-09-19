# -*- coding: utf-8 –*-
__author__ = 'Hu Wenchao'

from beautifulscraper import BeautifulScraper
import re
PROBLEM_NUMBER = 480
scraper = BeautifulScraper()

# 题目信息获取
#for number in xrange(1, PROBLEM_NUMBER+1):
number = 99
url = "https://projecteuler.net/problem=%d" % number
soup = scraper.go(url)
title = soup.h2.get_text()	# 获取题目标题
# problem_description = soup.find(role="problem").get_text()
# print problem_description	# 获取题目信息

