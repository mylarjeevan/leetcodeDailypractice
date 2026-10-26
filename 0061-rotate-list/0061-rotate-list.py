# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        
        temp=head
        size=0
        while temp is not None:
            size+=1
            temp=temp.next
        k=k%size
        if k==0 or head is None:
            return head
        step=size-k
        temp=head
        count=0
        while temp.next is not None:
            if count==step-1:
                ptr1=temp
                ptr2=temp.next
            count+=1
            temp=temp.next
        
        temp.next=head
        ptr1.next=None
        
        return ptr2



        