# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if right and left:
                return root
            return left or right

        return dfs(root, p, q)