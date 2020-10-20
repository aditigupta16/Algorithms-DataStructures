import re
from collections import defaultdict, Counter

def get_most_common_word(paragraph, banned_list):
    
    punctuation_symbols = ['!','?',';','.', ',']
    hash_map = defaultdict(int)

    paragraph = re.sub(r'[^\w]', ' ', paragraph).split(' ')
    
    for word in paragraph:
        if word == '':
            continue
        for symbol in punctuation_symbols:
            word = word.strip(symbol)
        word = word.lower()
        if word in banned_list:
            continue
        hash_map[word] += 1

    max_occurence = 0
    max_occuring_word = ''
    for word in hash_map:
        if hash_map[word] > max_occurence:
            max_occuring_word = word
            max_occurence = hash_map[word]
    return max_occuring_word









if __name__ == '__main__':
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned_list = ["a"]
    print(get_most_common_word(paragraph, banned_list))