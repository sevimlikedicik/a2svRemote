from helper.ListNode import ListNode


def has_cycle(head: ListNode):
    slow = head
    fast = head

    while fast:
        if fast.next:
            fast = fast.next.next
        else:
            return False
        slow = slow.next
        if slow == fast:
            return True
    return False
