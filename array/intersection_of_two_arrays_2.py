
from collections import Counter


def intersection_of_arrays_2(nums1, nums2):
    output = []
    intersection_count = dict(Counter(nums1) & Counter(nums2))
    for key, val in intersection_count.items():
        while val:
            output.append(key)
            val -=1
    return output


if __name__ == '__main__':

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersection_of_arrays_2(nums1, nums2))