from typing import Optional

from helper.ListNode import ListNode


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    walk = head
    prev = None

    while walk:
        next_node = walk.next
        walk.next = prev
        prev = walk
        walk = next_node

    return prev
