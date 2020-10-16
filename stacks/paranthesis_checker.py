

def paranthesis_check(s):
    if len(s) % 2:
        return False
    paranthesis_mapping = {']': '[', '}': '{', ')': '('}
    stack = []

    for bracket in s:
        if str(bracket) not in paranthesis_mapping:
            stack.append(bracket)
        else:
            if not stack or stack.pop()!=paranthesis_mapping[bracket]:
                return False
    if stack:
        return False
    return True


if __name__ == '__main__':
    s = '){})'
    print(paranthesis_check(s))