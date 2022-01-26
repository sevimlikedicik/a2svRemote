from math import inf
from typing import Optional

from helper.ListNode import ListNode


def pairSum(head: Optional[ListNode]) -> int:
    slow = head
    fast = head
    prev = None

    while fast:
        fast = fast.next.next
        slow_next = slow.next
        slow.next = prev
        prev = slow
        slow = slow_next

    max_ = -inf
    while slow:
        max_ = max(max_, slow.val + prev.val)
        slow = slow.next
        prev = prev.next

    return max_
