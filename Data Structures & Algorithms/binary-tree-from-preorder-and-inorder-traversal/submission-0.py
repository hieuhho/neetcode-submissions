# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_map = {val: idx for idx, val in enumerate(inorder)}
        start = 0
        def dfs(l, r):
            if l > r:
                return None
            nonlocal hash_map, start

            node = TreeNode(preorder[start])
            mid = hash_map[preorder[start]]
            start += 1
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)
            return node
        return dfs(0, len(inorder) - 1)