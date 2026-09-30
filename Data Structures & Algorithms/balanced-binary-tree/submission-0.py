# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            if not node:
                return 0
            
            left_depth = checkHeight(node.left)
            if left_depth == -1:
                return -1
            right_depth = checkHeight(node.right)
            if right_depth == -1:
                return -1
            if abs(right_depth-left_depth) >1:
                return -1

            return 1 + max(right_depth, left_depth)
        return checkHeight(root) != -1