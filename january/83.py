from typing import Optional

from helper.ListNode import ListNode


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    walk = head

    while walk and walk.next:
        if walk.next.val == walk.val:
            walk.next = walk.next.next
        else:
            walk = walk.next

    return head
