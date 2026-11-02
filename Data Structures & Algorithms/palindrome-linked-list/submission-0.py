# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #step 1: find mid point
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #step2: reverse second half
        second_half_head=self.reverse(slow)

        #step3: compare both the halves
        first_half_ptr=head
        second_half_ptr=second_half_head

        while second_half_ptr:
            if first_half_ptr.val!=second_half_ptr.val:
                return False
            first_half_ptr=first_half_ptr.next
            second_half_ptr=second_half_ptr.next
        
        return True

        
        

    # reverse linked list
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev



