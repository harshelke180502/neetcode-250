# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #iterative dfs
        stack=[root]
        #height,diameter of the visited node
        mp={None:[0,0]}
        while stack:
            node=stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                curr=stack.pop()
                left_height,left_diameter=mp[curr.left]
                right_height,right_diameter=mp[curr.right]
                mp[curr]=(1+ max(left_height,right_height),   max(left_diameter,right_diameter,left_height+right_height))
        
        return mp[root][1]






        #recursive dfs ()
        # self.res=0

        # def dfs(curr):
        #     if curr==None:
        #         return 0
            
        #     left=dfs(curr.left)
        #     right=dfs(curr.right)

        #     self.res=max(self.res,left+right)

        #     return 1+max(left,right)
        
        # dfs(root)
        # return self.res

                
        