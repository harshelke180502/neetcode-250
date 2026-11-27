# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # recursive way:

        if not root or not p or not q:
            return None
        if max(p.val,q.val)<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(p.val,q.val)>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else: 
            return root
    


            
        #there will be three cases : 1. when both vals are on opp ends or one of them is the root return cur, if both are on same ends(left or right) traverse through that path until they split somewhere
        #iterative way to do it
        # cur=root
        # while cur:
        #     if p.val>cur.val and q.val>cur.val:
        #         cur=cur.right
        #     elif p.val<cur.val and q.val<cur.val:
        #         cur=cur.left
        #     else:
        #         return cur







        


        