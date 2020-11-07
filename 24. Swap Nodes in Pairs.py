# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root=head
        temp=head
        result=None
        prev=None
        if temp==None or temp.next==None:
            return temp
        while temp.next:
            a=temp.next
            b=a.next
            temp.next.next=temp
            temp.next=b
            if prev !=None:
                prev.next=a
                prev=a.next
            else:
                prev=temp
            if result==None:
                result=a
            temp=b
            if temp == None:
                break
        return result
