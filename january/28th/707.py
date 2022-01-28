class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = Node(0)

    def get(self, index: int) -> int:
        walk = self.head.next
        count = 0

        while walk:
            print(walk.val)
            if count == index:
                return walk.val
            walk = walk.next
            count += 1

        return -1

    def addAtHead(self, val: int) -> None:
        head_next = self.head.next
        self.head.next = Node(val)
        self.head.next.next = head_next

    def addAtTail(self, val: int) -> None:
        if not self.head.next:
            self.head.next = Node(val)
            return

        walk = self.head.next
        while walk.next:
            walk = walk.next
        walk.next = Node(val)
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)

        walk = self.head.next
        count = 0

        while walk:
            if count == index - 1:
                walk_next = walk.next
                walk.next = Node(val)
                walk.next.next = walk_next
                return
            walk = walk.next
            count += 1

        return

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head.next:
                self.head.next = self.head.next.next

            return

        walk = self.head.next
        count = 0

        while walk:
            if count == index - 1 and walk.next:
                walk.next = walk.next.next
                return
            walk = walk.next
            count += 1

        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
