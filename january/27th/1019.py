from typing import Optional, List

from helper.ListNode import ListNode


def nextLargerNodes(head: Optional[ListNode]) -> List[int]:
    res = [0 for _ in range(10000)]
    walk = head
    stack = []
    stack_index = 0
    index = 0

    while walk:
        res[index] = walk.val
        while stack_index > 0 and walk.val > res[stack[stack_index - 1]]:
            res[stack[stack_index - 1]] = walk.val
            stack.pop()
            stack_index -= 1
        stack.append(index)
        stack_index += 1
        index += 1
        walk = walk.next

    for i in stack:
        res[i] = 0

    return res[0: index]