# -*- coding: utf-8 –*-
# 数字转英文包：https://pypi.python.org/pypi/num2words
# execute `pip install num2words` in shell before use this
from num2words import num2words
result = 0
for i in xrange(1, 1001):
	result += len(num2words(i).replace(' ','').replace('-',''))

print result

# 数字表参考：http://zh.wikibooks.org/zh/%E8%8B%B1%E8%AF%AD/%E8%8B%B1%E6%96%87%E6%95%B0%E5%AD%97
# dic = {
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine
# 10	ten
# 11	eleven	
# 12	twelve	
# 13	thirteen	
# 14	fourteen	
# 15	fifteen	
# 16	sixteen	
# 17	seventeen	
# 18	eighteen	
# 19	nineteen	
# 20	twenty	
# 30	thirty	
# 40	forty	
# 50	fifty	
# 60	sixty	
# 70	seventy	
# 80	eighty	
# 90	ninety	
# }