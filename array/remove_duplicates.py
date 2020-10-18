


def remove_duplicates(nums):
    temp = {}
    i = 0
    while i < len(nums):
        if nums[i] not in temp:
            temp[nums[i]] = True
        else:
            nums.pop(i)
        i += 1
    print(nums)
    return len(nums)







if __name__ == '__main__':

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(remove_duplicates(nums))