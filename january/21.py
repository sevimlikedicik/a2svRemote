from typing import Optional

from helper.ListNode import ListNode


# worst code ever
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not (list1 or list2):
        return None

    # dummy node
    head = ListNode(0)
    walk = head
    walk_1 = list1
    walk_2 = list2

    while walk_1 and walk_2:
        if walk_1.val < walk_2.val:
            walk.next = walk_1
            walk = walk.next
            walk_1 = walk_1.next
        else:
            walk.next = walk_2
            walk = walk.next
            walk_2 = walk_2.next

    if walk_1:
        while walk_1:
            walk.next = walk_1
            walk = walk.next
            walk_1 = walk_1.next
    else:
        while walk_2:
            walk.next = walk_2
            walk = walk.next
            walk_2 = walk_2.next

    return head.next
