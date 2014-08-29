__author__ = 'apple'
def largest_palindrome_from_digit(n):
    max_d = int('9'*n)
    min_d = int('1'+'0'*(n-1))
    l = range(max_d, min_d, -1)
    palindrome_list = []
    for i in l:
        for j in l:
            product = i*j
            if str(product) == str(product)[::-1]:
                palindrome_list.append(product)
    return palindrome_list

if __name__ == '__main__':
    print max(largest_palindrome_from_digit(3))
