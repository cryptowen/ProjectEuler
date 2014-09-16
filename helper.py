import math

def next_prime(prime_list):
    last_prime = prime_list[-1]
    while True:
        last_prime += 1
        is_prime = True
        for prime in prime_list:
            if last_prime % prime == 0:
                is_prime = False
                break
            if prime > math.sqrt(last_prime):   # sqrt is faster than last_prime/2
                break
        if is_prime:
            # print last_prime
            prime_list.append(last_prime)
            return prime_list

list_product = lambda l: reduce(lambda x,y:int(x)*int(y), l)        