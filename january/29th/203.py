from typing import Optional

from helper.ListNode import ListNode


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while head and head.val == val:
        head = head.next

    walk = head

    while walk and walk.next:
        if walk.next.val == val:
            walk.next = walk.next.next
        else:
            walk = walk.next

    return head
