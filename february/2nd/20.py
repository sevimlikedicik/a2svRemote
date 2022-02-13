def isValid(s: str) -> bool:
    complements = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []
    for c in s:
        if c in complements:
            if stack and stack.pop() == complements[c]:
                continue
            else:
                return False
        else:
            stack.append(c)

    return not stack
