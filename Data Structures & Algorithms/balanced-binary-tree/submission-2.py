# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        #recursive dfs

        def chk_height(node):
            if not node:
                return 0
            left=chk_height(node.left)
            if left==-1:
                return -1
            right=chk_height(node.right)
            if right==-1:
                return -1
            
            if abs(left-right)>1:
                return -1
            
            return 1+max(left,right)
        
        return chk_height(root)!=-1 
            
            
            

            
        
        
        
        #iterative dfs - to find balanced tree
        # if not root:
        #     return True

        # stack=[root]
        # height={None:0}
        # while stack:
        #     node=stack[-1]
        #     if node.left and node.left not in height:
        #         stack.append(node.left)
        #     elif node.right and node.right not in height:
        #         stack.append(node.right)
        #     else:
        #         node=stack.pop()
        #         left_h=height[node.left]
        #         right_h=height[node.right]
        #         if abs(left_h-right_h)>1:
        #             return False
        #         height[node]=1+max(left_h,right_h)

        # return True


        