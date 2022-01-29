from typing import Optional

from helper.ListNode import ListNode


def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    real_head = ListNode()
    real_head.next = head
    walk = real_head

    while walk.next:
        walk_start = walk
        sum_ = 0
        walk_end = walk.next

        while walk_end:
            sum_ += walk_end.val
            if sum_ == 0:
                break
            walk_end = walk_end.next

        if sum_ == 0:
            while walk_start.next != walk_end:
                walk_start.next = walk_start.next.next
            walk_start.next = walk_start.next.next
            walk = walk_start
        else:
            walk = walk.next

    return real_head.next
