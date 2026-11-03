# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        while curr:
            nxt=curr.next
            # nxt_val=curr.next.val
            if curr.val==val:
                prev.next=nxt
            else:
                prev=curr
            curr=curr.next
        return dummy.next

