

def get_next_greater_element_list(arr):
    next_greater_element_list = []

    stack = []
    i = 0
    while i < len(arr):
        stack.append(arr[i])
        j = i+1
        while j < len(arr):
            # until the number is greater than the stack keep pushing them in stack.
            if arr[j] < stack[-1]:
                stack.append(arr[j])
                j += 1
                i += 1
            else:
                # so all number in stack will have the same nge so append the nge in array
                while stack:
                    stack.pop()
                    next_greater_element_list.append(arr[j])
                break
        i += 1

    # if still any number left in stack then these many numbers don't have any nge
    while stack:
        next_greater_element_list.append(-1)
        stack.pop()
    print(next_greater_element_list)


if __name__ == '__main__':
    arr = [4, 5, 2, 25]
    get_next_greater_element_list(arr)