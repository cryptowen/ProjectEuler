__author__ = 'apple'

def next_prime(prime_list):
    '''
    :param prime_list: list of int
    :return: list of int
    >>> prime_list = [2]
    >>> next_prime(prime_list)
    [2, 3]
    >>> prime_list
    [2, 3]
    '''
    last_prime = prime_list[-1]
    while True:
        last_prime += 1
        is_prime = True
        for prime in prime_list:
            if last_prime % prime == 0:
                is_prime = False
                break
            if prime > last_prime/2:
                break
        if is_prime:
            prime_list.append(last_prime)
            return prime_list

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    prime_list = [2]
    for i in xrange(10000):
        next_prime(prime_list)
    print prime_list[-1]