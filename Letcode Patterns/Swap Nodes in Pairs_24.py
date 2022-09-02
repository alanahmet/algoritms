# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        result = ListNode(1)
        result_head = result
        while head:
            if head and head.next:
                result.next = ListNode(head.next.val)
                result = result.next
                result.next = ListNode(head.val)
                result = result.next
                head = head.next.next
            elif head:
                result.next = ListNode(head.val)
                result = result.next
                head = head.next
            if not head:
                break
        return result_head.next
