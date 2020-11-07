# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=ListNode(0)
        curr=result
        carry=0
        while l1 or l2:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            s=x+y+carry
            carry=s//10
            s=s%10
            curr.next=ListNode(s)
            curr=curr.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry>0:
            curr.next=ListNode(carry)
        return result.next
