# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=headA
        l2=headB
        lenA=0
        lenB=0
        while l1:
            l1=l1.next
            lenA+=1
        while l2:
            l2=l2.next
            lenB+=1

        l1=headA
        l2=headB

        if lenA>lenB:
            diff=lenA-lenB
            while diff:
                l1=l1.next
                diff-=1
        else:
            diff=lenB-lenA
            while diff:
                l2=l2.next
                diff-=1

        while l1!=l2:
            l1=l1.next
            l2=l2.next
        return l1
            

        

        # l1=headA
        # l2=headB
        # while l1!=l2:
        #     l1=l1.next if l1 else headB
        #     l2=l2.next if l2 else headA
        # return l2


        