# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length=1
        temp=head
        if temp==None:
            return temp
        while temp.next:
            length+=1
            temp=temp.next
        if length-n==0:
            return head.next
        temp=head
        while length-n-1:
            length-=1
            temp=temp.next
        temp.next=temp.next.next
        return head
       
