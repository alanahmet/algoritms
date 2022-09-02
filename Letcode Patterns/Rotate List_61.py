# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return None
        l = 0
        dummyH = head
        while dummyH:
            l += 1
            dummyH = dummyH.next

        k = k % l
        i = 0
        dummyH = copy.copy(head)

        resH = head
        dumR = resH
        while dummyH and i != l - k:
            i += 1
            dummyH = dummyH.next
            if not i == l - k - 1:
                dumR = dumR.next
        dumR.next = None
        h = dummyH
        while dummyH and dummyH.next:
            dummyH = dummyH.next
        dummyH.next = resH
        return h

        return None
