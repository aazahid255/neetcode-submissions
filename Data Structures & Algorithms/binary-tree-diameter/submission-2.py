# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: binary tree
# output: diameter of tree
# edge cases: empty tree

# mtch: dfs, tree

# plan: number of edges in a path is the diameter

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            nonlocal res
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return 1 + max(dfs(root.left), dfs(root.right))
        

        dfs(root)
        return res
        