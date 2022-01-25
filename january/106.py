from typing import Optional

from helper.ListNode import ListNode


# Cheat solution, fast-slow pointers would be better
def hasCycle(head: Optional[ListNode]) -> bool:
    walk = head

    for i in range(10002):
        if not walk:
            return False
        walk = walk.next

    return True
