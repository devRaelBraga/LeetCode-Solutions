# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #42ms beats 99,41%
        carry = 0

        result = ListNode()
        root = result

        while l1 or l2 or (carry > 0):
            sum = 0
            sum += carry
            carry = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum >= 10:
                sum -= 10
                carry = 1

            result.val = sum
            
            result.next = ListNode() if l1 or l2 or (carry > 0) else None
            result = result.next
        return root
