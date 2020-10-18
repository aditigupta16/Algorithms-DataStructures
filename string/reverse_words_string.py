
# reverse the string with words as with each char reversed


def reverse_word(word):
    reversed_word = ''
    for i in range(len(word)-1, -1, -1):
        reversed_word += word[i]
    print(reversed_word)


if __name__ == "__main__":

    word = 'i love programming very much.'
    reverse_word(word)