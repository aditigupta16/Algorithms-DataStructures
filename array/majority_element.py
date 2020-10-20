from collections import defaultdict
import math


def majority_element(nums):
    count_dict = defaultdict(int)
    arr_length = math.floor(len(nums)/2)
    for element in nums:
        count_dict[element] += 1
        if count_dict[element] > arr_length:
            return element
    


if __name__ == '__main__':
	print(majority_element([3,2,3]))

