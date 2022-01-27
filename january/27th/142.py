from typing import Optional

from helper.ListNode import ListNode


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if not fast or not fast.next:
        return None

    new_slow = head

    while True:
        slow_start = slow
        slow = slow.next
        while new_slow != slow and slow_start != slow:
            slow = slow.next

        if new_slow == slow:
            return new_slow
        else:
            new_slow = new_slow.next


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
cycle = detectCycle(head)

for _ in range(20):
    print(cycle.val)
    cycle = cycle.next
