

def string_matching(words):
    output = []
    
    i = 0
    while i < len(words):
        j = 0
        while j < len(words):
            if i == j:
                j+=1
                continue
            if words[i] in words[j]:
                output.append(words[i])
                break
            j += 1    
        i += 1 
    return output





if __name__ == '__main__':
    words = ["blue","green","bu"]
    print(string_matching(words))