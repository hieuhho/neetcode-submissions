# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # use a list so we don't have to use nonlocal inside dfs
        ans = [root.val]
        def dfs(node):
            if not node:
                return 0

            left =  dfs(node.left)
            right = dfs(node.right)
            left_max = max(left, 0)
            right_max = max(right, 0)

            # update answer with sum of current node with left & right
            ans[0] = max(ans[0], node.val + left_max + right_max)
            # return max of current node sum
            return node.val + max(left_max, right_max)

        dfs(root)
        return ans[0]