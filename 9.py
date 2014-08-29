__author__ = 'apple'
import itertools
def triplet_below_n(num):
    for i, j in itertools.combinations_with_replacement(range(1, num+1),2):
        num_list = [i, j, num-i-j]
        num_list.sort()
        if num_list[0] + num_list[1] <= num_list[2]:
            continue
        if num_list[0] * num_list[0] + num_list[1] * num_list[1] == num_list[2] * num_list[2]:
            print num_list
            return num_list[0]*num_list[1]*num_list[2]

if __name__ == "__main__":
    print triplet_below_n(1000)