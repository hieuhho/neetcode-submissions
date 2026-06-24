# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, high_val):
            if not node:
                return 0
            
            ans = left = right = 0
            if node.val >= high_val:
                ans += 1
            if node.val > high_val:
                high_val = node.val
            if node.left:
                left = dfs(node.left, high_val)
            if node.right:
                right = dfs(node.right, high_val)
            return ans + left + right
        return dfs(root, root.val)