from collections import defaultdict
import math


def max_consecutive_ones(nums):
    max_occurence = 0
    i = 0
    while i < len(nums):
        occurence = 0
        while nums[i] == 1:
            occurence += 1
            i += 1
            if i >= len(nums):
                break
        if occurence > max_occurence:
            max_occurence = occurence
        i +=1
    return max_occurence



if __name__ == '__main__':
    print(max_consecutive_ones([1,1,0,0,1,1,1,1]))

