# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        queue = deque([root])
        while queue:
            queue_len = len(queue)
            current_depth = []
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    current_depth.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if current_depth:
                ans.append(current_depth)
        return ans