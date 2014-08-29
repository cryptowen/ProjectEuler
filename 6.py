__author__ = 'apple'
def sum_of_square(num_list):
    '''
    :param num_list: list of int
    :return: int
    >>> sum_of_square(range(1,11))
    385
    '''
    return sum([i*i for i in num_list])

def square_of_sum(num_list):
    '''
    :param num_list: list of int
    :return: int
    >>> square_of_sum(range(1,11))
    3025
    '''
    sum_num_list = sum(num_list)
    return sum_num_list * sum_num_list

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    num_list = range(1, 101)
    print square_of_sum(num_list) -sum_of_square(num_list)