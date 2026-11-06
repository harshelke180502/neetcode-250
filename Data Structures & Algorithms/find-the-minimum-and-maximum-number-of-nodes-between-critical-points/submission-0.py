# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    


    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        def critical(prev,curr,nxt):
            return ( (prev.val>curr.val<nxt.val) or (nxt.val<curr.val>prev.val) )

        prev,curr=head,head.next
        nxt=curr.next
        prev_critical_idx=0
        first_critical_idx=0
        min_dist=float("inf")
        max_dist=-1
        i=1
        while nxt:
        
            if critical(prev,curr,nxt):
                if first_critical_idx:
                    max_dist=i-first_critical_idx
                    min_dist=min(min_dist,i-prev_critical_idx)
                else:
                    first_critical_idx=i

                prev_critical_idx=i

            prev,curr,nxt=curr,nxt,nxt.next
            i+=1
        if min_dist==float("inf"):
            min_dist=-1
        return [min_dist,max_dist]



       
     

            
                

                
                




