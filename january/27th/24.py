from typing import Optional

from helper.ListNode import ListNode


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = ListNode()
    prev.next = head
    walk = head
    head = prev

    while walk and walk.next:
        next_node = walk.next
        walk = walk.next.next
        next_node.next = prev.next
        next_node.next.next = walk
        prev.next = next_node
        prev = next_node.next

    return head.next
