# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem, res = 0, l1
        while l1 or l2:
            l1S = l1.val if l1 else 0
            l2S = l2.val if l2 else 0
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()
            summ = l1S + l2S + rem
            rem = summ // 10
            l1.val = summ % 10
            l1, l2 = l1.next, l2.next
        if rem:
            l1 = ListNode(rem)
        return res
