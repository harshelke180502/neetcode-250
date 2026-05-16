"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldtonew={}
        copy=Node(node.val)
        oldtonew[node]=copy
        queue=deque([node])

        while queue:
            curr=queue.popleft()

            for nei in curr.neighbors:
                if nei not in oldtonew:
                    oldtonew[nei]=Node(nei.val)
                    queue.append(nei)
                oldtonew[curr].neighbors.append(oldtonew[nei])
        return oldtonew[node]

        # def dfs(node):
        #     if node in oldtonew:
        #         return oldtonew[node]
        #     copy=Node(node.val)
        #     oldtonew[node]=copy
        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))
        #     return copy
        # return dfs(node) if node else None
                            