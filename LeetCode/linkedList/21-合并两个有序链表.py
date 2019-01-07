# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(None)
        cur = dummyHead

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next, cur, l1 = l1, l1, l1.next

            else:
                cur.next, cur, l2 = l2, l2, l2.next

        if l1 == None:
            cur.next = l2

        if l2 == None:
            cur.next = l1

        return dummyHead.next
