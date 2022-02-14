def decodeAtIndex(s: str, k: int) -> str:
    index = 0
    stack = []

    for c in s:
        if c.isalpha():
            index += 1
        else:
            index *= int(c)
        stack.append(c)

        if index >= k:
            while stack:
                val = stack.pop()
                if val.isalpha():
                    if index == k:
                        return val
                    index -= 1
                else:
                    index //= int(val)
                    k %= index
                    if k == 0:
                        k = index
