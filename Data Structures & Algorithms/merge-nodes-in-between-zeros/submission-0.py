# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail,curr,total=dummy,head.next,0
        while curr:
            if curr.val==0:
                tail.next=ListNode(total)
                tail=tail.next
                total=0
            else:
                total+=curr.val
            curr=curr.next
        return dummy.next
        