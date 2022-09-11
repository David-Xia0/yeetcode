# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, max, min):
            if root is None:
                return True

            if root.val >= max or root.val <= min:
                return False

            return dfs(root.left, root.val, min) and  dfs(root.right, max, root.val)


        return dfs(root, float('inf'), float('-inf'))