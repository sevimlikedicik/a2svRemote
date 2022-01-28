from math import inf
from typing import List, Optional

from helper.ListNode import ListNode


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    head = ListNode()
    walk = head

    while None in lists: lists.remove(None)

    while lists:
        min_ = inf
        for i in range(len(lists)):
            if lists[i].val < min_:
                min_ = lists[i].val
                ind = i

        walk.next = ListNode(min_)
        walk = walk.next
        lists[ind] = lists[ind].next

        if not lists[ind]:
            lists.remove(None)

    return head.next
