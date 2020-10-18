from itertools import permutations
# check if permutation of s1 is in s2 (brute force)

def permutation_in_string(s1, s2):
    s1_permutations = [s for s in permutations(s1)]
    string_perms = []
    for perm in s1_permutations:
        string = ''
        for char in perm:
            string += char
        string_perms.append(string)

    return(any(string for string in string_perms if string in s2))


if __name__ == '__main__':
    s1 = 'ab'
    s2 = 'eidboaoo'
    print(permutation_in_string(s1, s2))