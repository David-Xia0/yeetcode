# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = head, head

        while right.next is not None:
            right = right.next
            left = left.next
            if right.next is None:
                return left
            right = right.next

        return left
            