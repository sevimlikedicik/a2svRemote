from typing import Optional

from helper.ListNode import ListNode


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    slow_next = slow.next
    slow.next = None
    slow = slow_next
    while slow:
        slow_next = slow.next
        slow.next = prev
        prev = slow
        slow = slow_next

    slow_2 = prev
    slow = head
    while slow and slow_2:
        slow_next = slow.next
        slow.next = slow_2
        slow = slow_next
        slow_2_next = slow_2.next
        slow_2.next = slow
        slow_2 = slow_2_next

    return head
