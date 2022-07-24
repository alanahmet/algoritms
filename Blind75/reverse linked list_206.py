class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    def print_it(self,head):
        d_head = head
        while d_head:
            print(d_head.val)
            d_head = d_head.next

print(Solution().reverseList())