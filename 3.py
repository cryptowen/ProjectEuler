def next_prime(prime_list):
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

prime_list = [2]
number = 600851475143
i = 0
while number != 1:
    if i >= len(prime_list):
        next_prime(prime_list)
        continue
    if number%prime_list[i]==0:
        number /= prime_list[i]
        max_prime = prime_list[i]
    else:
        i += 1

print max_prime


