# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from collections import deque


class Solution:
    def levelOrderBFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        level = 0
        q = deque()
        q.append((root,level))

        ans = [[]]

        while len(q) != 0:
            (node, currLevel) = q.popleft()
            if currLevel == level:
                ans[-1].append(node.val)
            else:
                level += 1
                ans.append([node.val])
            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))

        return ans

    def levelOrderDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def level(ans, root, h):
            if root is None:
                return
            
            if h >= len(ans):
                ans.append([])
            
            ans[h].append(root.val)
            level(ans, root.left, h+1)
            level(ans, root.right, h+1)

        level(ans, root, 0)
        return ans
