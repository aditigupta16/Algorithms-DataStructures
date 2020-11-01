from collections import defaultdict
import math


def k_diff_pairs(nums,k):
    k_diff_pair = []
    nums = sorted(nums)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+k==nums[j]:
                k_diff_pair.append((nums[i],nums[j]))
            elif nums[i]+k < nums[j]:
                break

            
    return len(set(k_diff_pair))



if __name__ == '__main__':
    nums=[1,2,3,4,5]
    k=1
    
    print(k_diff_pairs(nums,k))

