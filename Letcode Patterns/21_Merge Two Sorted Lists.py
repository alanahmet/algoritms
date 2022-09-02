# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        l3 = ListNode(0)
        dummy = l3
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                new_node = ListNode(l1.val)
                l1 = l1.next
            else:
                new_node = ListNode(l2.val)
                l2 = l2.next

            l3.next = new_node
            l3 = l3.next

        while l1 != None:
            new_node = ListNode(l1.val)
            l3.next = new_node
            l3 = new_node
            l1 = l1.next

        while l2 != None:
            new_node = ListNode(l2.val)
            l3.next = new_node
            l3 = new_node
            l2 = l2.next

        return dummy.next