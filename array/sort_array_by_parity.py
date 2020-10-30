import collections

def sort_array_by_parity(nums):
    output = []
    hash_map = collections.defaultdict(list)

    for num in nums:
        if num%2:
            hash_map['odd'].append(num)
        else:
            hash_map['even'].append(num)

    for i in range(len(hash_map['even'])):
        output.append(hash_map['even'][i])
        output.append(hash_map['odd'][i])
    return output



if __name__ == '__main__':
    nums = [4,2,5,7]
    print(sort_array_by_parity(nums))