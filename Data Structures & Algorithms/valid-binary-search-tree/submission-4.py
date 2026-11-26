# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: root of binary ree
# output: boolean, true or false if it is a valid bst
# edge cases: empty root, onyl one root in tree, both would be valid

# inorder traversal
# isValidBST(root.left)
# check current node
# isValidBST(root.right)
# do an inorder traversal, if the current node is ever smaller than the largest seen so far, we do not have a valid bst


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        def inorder(root):
            nonlocal prev
            if not root:
                return True
            if not inorder(root.left) : return False
            if root.val <= prev:
                return False
            prev = max(prev, root.val)
            if not inorder(root.right): return False
            return True
        return inorder(root)
        
        