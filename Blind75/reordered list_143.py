import copy

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #reverse the list and count them
        prev = None
        c_head = copy.deepcopy(head)
        count = 0
        while c_head:
            count+=1
            curr = c_head
            c_head = c_head.next
            curr.next = prev
            prev = curr
        #add iterativly
        r_head =  res = ListNode(0)
        for i in range(count//2):
            res.next = head
            head = head.next
            res = res.next
            res = prev
            prev = prev.next
        print(r_head)