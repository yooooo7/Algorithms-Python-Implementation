class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(None)
        self.len = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.len - 1 < index:
            return -1

        lastNode = self.head
        for i in range(index):
            lastNode = lastNode.next

        return lastNode.next.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        curNode = ListNode(val)
        curNode.next, self.head.next = self.head.next, curNode
        self.len += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        lastNode = self.head
        curNode = ListNode(val)
        while lastNode.next is not None:
            lastNode = lastNode.next

        lastNode.next = curNode
        self.len += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if self.len < index:
            return -1

        curNode = ListNode(val)
        lastNode = self.head
        for i in range(index):
            lastNode = lastNode.next

        curNode.next, lastNode.next = lastNode.next, curNode
        self.len += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.len - 1 < index:
            return -1

        lastNode = self.head
        for i in range(index):
            lastNode = lastNode.next

        lastNode.next = lastNode.next.next
        self.len -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
