# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):
            prev=None
            curr=head
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        
        def return_no(head):
            res=""
            curr=head
            while curr:
                res+=str(curr.val)
                curr=curr.next
            return int(res)

        first=return_no(reverse(l1))

        second=return_no(reverse(l2))
       
        total=first+second
        # print("Total:",total)
        dummy=ListNode(0)
        prev=dummy
        digits = [int(d) for d in str(total)]
        print(digits)
        for i in digits:
            curr=ListNode(i)
            prev.next=curr
            prev=curr
        
        final=reverse(dummy.next)
        
        return final            





        
