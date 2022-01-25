from typing import Optional

from helper.ListNode import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # dummy node
    new_head = ListNode()
    carry = 0
    walk = new_head
    while l1 or l2:
        digit_sum = carry
        if l1:
            digit_sum += l1.val
            l1 = l1.next
        if l2:
            digit_sum += l2.val
            l2 = l2.next
        walk.next = ListNode(digit_sum % 10)
        walk = walk.next
        carry = digit_sum // 10

    if carry:
        walk.next = ListNode(1)

    return new_head.next
