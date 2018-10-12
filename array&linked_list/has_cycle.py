# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 检测链表中是否存在环（快慢指针）
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
        return False

    # 检测链表中是否存在环（集合判断）
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        prev, cur = set(), head
        while cur:
            prev.add(cur)
            cur = cur.next

            if cur in prev:
                return True
        return False
