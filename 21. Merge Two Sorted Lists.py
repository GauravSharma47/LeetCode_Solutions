# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l=list()
        while l1 or l2:
            if l1:
                l.append(l1.val)
                l1=l1.next
            if l2:
                l.append(l2.val)
                l2=l2.next
        l.sort()
        curr=ListNode(0)
        result=curr
        for i in l:
            result.next=ListNode(i)
            result=result.next
        return curr.next

            
