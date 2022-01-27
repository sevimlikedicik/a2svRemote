from typing import Optional

from helper.ListNode import ListNode


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    odd_head = head
    even_head = head.next
    odd_walk = odd_head
    even_walk = even_head

    while odd_walk.next.next:
        odd_walk.next = odd_walk.next.next
        odd_walk = odd_walk.next
        if odd_walk.next:
            even_walk.next = even_walk.next.next
            even_walk = even_walk.next
        else:
            break

    odd_walk.next = even_head
    even_walk.next = None

    return odd_head
