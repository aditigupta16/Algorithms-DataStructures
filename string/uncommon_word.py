from collections import defaultdict


def uncommon_word(A, B):
    A = A.split(' ')
    B = B.split(' ')
    output = []
    ref_dict = defaultdict(int)
    for word in A:
        ref_dict[word] += 1
    for word in B:
        ref_dict[word] += 1

    for word in ref_dict:
        if ref_dict[word] == 1:
            output.append(word)

    return output



if __name__ == '__main__':
    sentence1 = "apple apple"
    sentence2 = "banana"
    print(uncommon_word(sentence1, sentence2))