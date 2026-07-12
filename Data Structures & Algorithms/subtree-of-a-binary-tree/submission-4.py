# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# input: 2 trees, one root and one subroot
# output: a boolean true or false if the tree is a subroot
# edge cases: empty tree, tree is a subroot of itself

# match: dfs recursion

# plan:
# if both nodes are null, we can return true
# if both nodes exist, but are different, we have to recurse and check if they are eventually similar
# we dont want to start our checking until the roots are equal

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
   

    def sameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        if root1.val == root2.val:
            return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
        