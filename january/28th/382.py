from random import randint
from typing import Optional

from helper.ListNode import ListNode


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.size = 0
        self.head = head
        while head:
            self.size += 1
            head = head.next

    def getRandom(self) -> int:
        ind = randint(0, self.size - 1)
        walk = self.head
        for i in range(ind):
            walk = walk.next

        return walk.val
