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
        
        def converter(number):
            ans=0
            if number==0:
                return ans
            i=0
            while number>0:
                a=number%10
                ans+=a*(2**i)
                i+=1
                number=number//10
            return ans
            
            
        val=0
        temp=head
        while temp is not None:
            val=val*10+temp.val
            temp=temp.next
        return converter(val)
        