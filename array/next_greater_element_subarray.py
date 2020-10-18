

def get_next_greater_element_list(nums1, nums2):

    next_greater_element_list = []

    next_greater_element_list = []
    for num in nums1:
        found_flag = False
        nums_2_index = nums2.index(num)
        if nums_2_index == len(nums2)-1:
            next_greater_element_list.append(-1)
            continue

        for i in range(nums_2_index+1, len(nums2)):
            if nums2[i] > num:
                next_greater_element_list.append(nums2[i])
                found_flag = True
                break
        if not found_flag:
            next_greater_element_list.append(-1)

    print(next_greater_element_list)
                

if __name__ == '__main__':
    get_next_greater_element_list([1,3,5,2,4], [5,4,3,2,1])
