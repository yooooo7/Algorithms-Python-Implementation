# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(None)
        header = dummyHead
        carry = 0

        while l1 is not None or l2 is not None:
            if l1 is not None:
                num_l1 = l1.val
                l1 = l1.next
            else:
                num_l1 = 0

            if l2 is not None:
                num_l2 = l2.val
                l2 = l2.next
            else:
                num_l2 = 0

            num = carry + num_l1 + num_l2
            value = num % 10

            header.next = ListNode(value)
            header = header.next
            carry = num // 10

        if carry != 0:
            header.next = ListNode(carry)

        return dummyHead.next
