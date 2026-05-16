# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0
        
        #Check if l1 is 0 or non zero if its non zero then extract val else assign it to zero 
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            val=v1+v2+carry

            #the carry belongs to the leftmost no or element
            carry=val//10
            # the value belongs to the rightmost no in case of a 2 digit no like 15 or 27
            val=val%10
            curr.next=ListNode(val)
            
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
           
        return dummy.next
