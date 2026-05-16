"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy={None:None}

        cur=head

       #This loop is used to store the copy of the nodes
        while cur:
            copy=Node(cur.val)
            oldToCopy[cur]=copy
            cur=cur.next
            
        #This loop is used to link the nodes to each other
        cur=head
        while cur:
            
            copy=oldToCopy[cur]
            copy.next=oldToCopy[cur.next]
            copy.random=oldToCopy[cur.random]
            cur=cur.next
        
        return oldToCopy[head]
