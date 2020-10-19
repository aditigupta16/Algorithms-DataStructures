






from collections import defaultdict

def relative_sorting(arr1, arr2):
    output = []
    hash_map = {}
    not_present_elements = []
    
    for element in arr2:
        appearance_count = arr1.count(element)
        if appearance_count:
            hash_map[element] = True
        while appearance_count > 0:
            output.append(element)
            appearance_count -= 1

    for element in arr1:
        if element not in hash_map:
            not_present_elements.append(element)
    return output + sorted(not_present_elements)








if __name__ == '__main__':
    arr1 = [2,3,1,3,2,4,6,19,9,2,7]
    arr2 = [2,1,4,3,9,6]
    print(relative_sorting(arr1, arr2))