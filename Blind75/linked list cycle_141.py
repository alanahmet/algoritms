# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: []) -> bool:
        d = head
        o = head
        while d:
            d = d.next
            if d is None:
                return False
            if d == o:
                return True
            o = o.next
        return False