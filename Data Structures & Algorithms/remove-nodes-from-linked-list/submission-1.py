# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #O(1)- using reverse tice o(1) space
        def reverse(head):
            prev,curr=None,head
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        
        head=reverse(head)
        curr=head
        max_val=curr.val
        while curr.next:
            if curr.next.val<max_val:
                curr.next=curr.next.next
            else:
                max_val=curr.next.val
                curr=curr.next
        return reverse(head)



        
        
        #O(n)- using a stack and checking the topc element and popping it 
        stack=[]
        curr=head
        while curr:
            while stack and curr.val>stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr=curr.next

        dummy=ListNode(0)
        curr=dummy
        
        for n in stack:
            curr.next=ListNode(n)
            curr=curr.next
        return dummy.next
        


                
            

        

