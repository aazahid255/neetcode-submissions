# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: tree node, p and q node
# output: return the lowest common ancestor
# edge cases: empty tree: p or q empty, only one node in tree

# dfs
# start at root
# if root.val < p.val and root.val < q.val, then the lca is in the right tree. curr = curr.right
# if root.val > btoh, then step into left ree bc its smaller
# anything else, we are at the split point. return curr

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

        