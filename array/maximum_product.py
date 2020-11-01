from collections import defaultdict
import math


def maximum_product(nums):
    nums = sorted(nums)
    max_product = max((nums[0]*nums[1]*nums[-1]),(nums[-1]*nums[-2]*nums[-3]))
    return max_product




if __name__ == '__main__':
    print(maximum_product([1,2,3]))

