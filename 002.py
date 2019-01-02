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
        carry = 0
        final = dummyList = ListNode(carry)
        while l1 is not None or l2 is not None:
            val = carry
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val+=l2.val
                l2 = l2.next
                
            carry = val//10
            res = val%10
            final.next = ListNode(res)            
            final = final.next
        if carry:
            final.next = ListNode(carry)
            
        return dummyList.next
