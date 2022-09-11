# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, res = self.height(root)
        return res
 

    def height(self, root):
        if root is None:
            return 1, True

        left_h, left_b = self.height(root.left)
        if left_b == False:
            return 0, False

        right_h, right_b = self.height(root.right)
        if right_b == False:
            return 0, False

        if abs(right_h - left_h) > 1:
            return 0, False
        return max(right_h, left_h) + 1, True
