# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        _, d = self.recursive(root)
        return d

    def recursive(self, root):
        if root.left is None and root.right is None:
            return 1, 0
        
        l_l, l_d = 0, 0
        if root.left:
            l_l, l_d = self.recursive(root.left) 
        r_l, r_d = 0, 0
        if root.right:
            r_l, r_d = self.recursive(root.right)

        d = max(l_d, r_d)
        return max(l_l, r_l) + 1, max(d, l_l + r_l)
        


