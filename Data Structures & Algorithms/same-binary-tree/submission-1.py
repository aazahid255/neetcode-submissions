# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: 2 binary trees
# output: boolean values, if it is true of false
# edge cases: tree is empty

# match: dfs

# plan:
# recurse through both trees at the same time and cmpare if their left and right subtrees are the same


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False
        if not q and p:
            return False
        if not q and not p:
            return True
        if p.val != q.val:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        