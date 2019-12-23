"""
Balanced Brackets
"""

def balancedBrackets(s):

    opening = ["[", "{", "("]
    closing = ["]", "}", ")"]

    stack = []

    for b in s:
        if b in opening:
            stack.append(b)
        elif b in closing:
            if stack[len(stack)-1] == opening[closing.index(b)]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True

    return False


print(balancedBrackets("{}[]()"))

print(balancedBrackets("{}[]()["))

print(balancedBrackets("{{}[]()["))
