# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        leftprev=dummy
        cur=head

        # Step1:Moving upto left most element

        for i in range(left-1):
            leftprev=cur
            cur=cur.next
        
        #Step 2: Changing the pointers
        prev=None
        for i in range(right-left+1):
            tempnext=cur.next
            cur.next=prev
            prev=cur
            cur=tempnext
        
        #Step 3: moving the leftmost element to the end or the rightmost 
        leftprev.next.next=cur
        leftprev.next=prev

        return dummy.next
        