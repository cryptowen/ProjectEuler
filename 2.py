a = 1
b = 1		
sum = 0
while b<4000000:
    if b%2==0:
#	print b,
        sum += b
    a, b = b, a+b
print sum
