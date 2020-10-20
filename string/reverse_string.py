

import math



def reverse_string(string):
    limit = math.floor(len(string)/2)
    i = 0
    while i < limit:
        string[i], string[-(i+1)] = string[-(i+1)], string[i]
        i += 1
    return string










if __name__ == '__main__':
    s = ["H","a","n","n","a","h"]
    print(reverse_string(s))