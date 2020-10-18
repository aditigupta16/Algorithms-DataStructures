
def reverse_word(word):
    reversed_word = ''
    index = len(word) - 1

    while index >= 0:
        word_length = 0
        while word[index]!= ' ' and index >= 0:
            word_length += 1
            index -= 1
        reversed_word += (word[index+1:index+word_length+1] + ' ').replace(' +','')
        while word[index] == ' ':
            index -= 1
    print(reversed_word)

if __name__ == '__main__':
    word = 'a good   example'
    reverse_word(word)