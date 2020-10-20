


def add_strings(num1, num2):
    num1 = ''.join(reversed(num1))
    num2 = ''.join(reversed(num2))

    num1_len = len(num1)
    num2_len = len(num2)

    carry = 0
    output = ''

    if num1_len > num2_len:
        num2 = num2 + str(0)*(num1_len-num2_len)
        string_length = num1_len
    
    else:
        num1 = num1 + str(0)*(num2_len-num1_len)
        string_length = num2_len




    for i in range(string_length):
        sum_output = int(num1[i]) + int(num2[i]) + carry
        if sum_output >= 10:
            carry = 1
            sum_output -= 10
        else:
            carry = 0
        output += str(sum_output)
    if carry:
        output += str(1)
    output = ('').join(reversed(output))
    return output







if __name__ == '__main__':
    num1 = '99'
    num2 = '990'

    print(add_strings(num1, num2))
