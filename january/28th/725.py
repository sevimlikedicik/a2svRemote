from typing import Optional, List

from helper.ListNode import ListNode


def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    list_size = 0
    walk = head

    while walk:
        list_size += 1
        walk = walk.next

    part_sizes = [list_size // k for _ in range(k)]

    for i in range(list_size % k):
        part_sizes[i] += 1

    walk = head
    parts = []

    for size in part_sizes:
        part_head = walk
        parts.append(part_head)

        for _ in range(size - 1):
            walk = walk.next

        if not walk:
            continue

        walk_next = walk.next
        walk.next = None
        walk = walk_next

    return parts
