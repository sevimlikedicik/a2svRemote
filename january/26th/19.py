from typing import Optional

from helper.ListNode import ListNode


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    prev = head
    walk = head

    for _ in range(n + 1):
        if not walk:
            return prev.next
        walk = walk.next

    while walk:
        walk = walk.next
        prev = prev.next

    prev.next = prev.next.next

    return head
