# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 0
        b = ListNode()
        bHead = b
        while head:
            i += 1
            if i == left:
                res = ListNode()
                resHead = res
                while i <= right:
                    curr = head
                    head = head.next
                    curr.next = res
                    res = curr
                    i += 1
                if head:
                    resHead.val = head.val
                    if head.next:
                        resHead.next = head.next
                if res and res.val != 0:
                    b.next = res
                return bHead.next
            b.next = ListNode(head.val)
            b = b.next
            head = head.next
