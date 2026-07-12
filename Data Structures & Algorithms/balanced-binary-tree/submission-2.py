# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# input: binary tree
# output: boolean, if it is balance or not
# edge cases: empty tree

# match: dfs, recursion

# plan: get height at each node. if the height of left and right subtree differ by more than 1, return false
# if we get thrugh the recursion, we can return true

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        balanced = True
        
        def dfs(root):
            nonlocal balanced
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            print(abs(left - right))
            if abs(left - right) > 1:
                balanced = False

            return 1 + max(dfs(root.left), dfs(root.right))
        dfs(root)
        return balanced        