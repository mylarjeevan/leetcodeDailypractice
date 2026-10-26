# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        val=""
        temp=head
        while temp is not None:
            val+=str(temp.val)
            temp=temp.next
        return int(val,2)
        