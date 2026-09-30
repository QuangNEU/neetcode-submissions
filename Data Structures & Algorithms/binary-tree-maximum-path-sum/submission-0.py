# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 
            if not node.left and not node.right:
                self.res = max(self.res, node.val)
                return node.val
            
            if not node.left:
                left = 0
            else:
                left= dfs(node.left)
            if not node.right:
                right = 0
            else:
                right = dfs(node.right)
            max_val = max(left+right+node.val, node.val+left, node.val + right, node.val)
            self.res = max(self.res, max_val)   

            return max(node.val+left, node.val + right, node.val)
        dfs(root)
        return self.res