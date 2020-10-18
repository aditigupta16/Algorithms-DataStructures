

def move_zeroes(nums):
    import ipdb;ipdb.set_trace()
    i = 0; j = 0

    while i < len(nums):
        if nums[i] == 0:
            y j< len(nums):
                if nums[j] == 0:
                    j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
    
    


if __name__ == '__main__':
    nums = [0,1,0,3,12]
    print(move_zeroes(nums))