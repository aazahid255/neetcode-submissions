# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: root of a binary tree
# output; integer, which is the depth of the tree
# edge cases: empty root, only one node in root 

# recursive, use max funciton

# if not root: return 0
# return 1 + max(maxDepth(root.left) + (maxDepth(root.rigt)))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), (self.maxDepth(root.right)))

        