from typing import Optional

from helper.ListNode import ListNode


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    mid = head
    end = head

    while end:
        end = end.next
        if end:
            end = end.next
        else:
            return mid
        mid = mid.next

    return mid