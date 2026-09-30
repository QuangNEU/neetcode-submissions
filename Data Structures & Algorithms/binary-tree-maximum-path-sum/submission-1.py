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
                return 0
            
            left = max(dfs(node.left),0)
            right = max(dfs(node.right), 0)

            max_val = node.val + left + right
            self.res = max(self.res, max_val)

            return node.val + max(left, right)
        dfs(root)
        return self.res