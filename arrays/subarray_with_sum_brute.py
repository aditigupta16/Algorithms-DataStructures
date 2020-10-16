# Brute force algorithm to found a subarray with a given sum.
# Iterates over each element and then starts to create the array from there and if sum found
# return the relevant array 
# Complexity - Time: O(n^2)
#            - Space: O(1) as always 1 extra array is created inrrespective of the length of arr



def subarray_with_given_sum(arr, target_sum):
    for i in range(len(arr)):
        computed_sum = arr[i]
        if computed_sum == target_sum:
            return [arr[i]]
        
        for j in range(i+1,len(arr)):
            computed_sum += arr[j]
            if computed_sum == target_sum:
                return arr[i:j+1]
            
            if computed_sum > target_sum:
                break
            
    return 'Sorry! no subarray found with given sum.'


if __name__ == "__main__":
    arr = [1, 4, 20, 3, 10, 5]
    target_sum = 18
    print(subarray_with_given_sum(arr, target_sum))
