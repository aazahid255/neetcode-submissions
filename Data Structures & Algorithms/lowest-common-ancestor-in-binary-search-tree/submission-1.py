# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# input: bst, 2 nodes from the tree
# output: the lowest common ancestor between the 2 nodes

# edge cases: empty tree, 1 of the nodes empty, both nodes could be empty, same node 

# match: tree, dfs

# brute force: go through ancestors of both nodes. once we have a list of all the ancestors, find the matches, return the lowest

# how to know if something is an ancestor?

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if(q.val > cur.val and p.val > cur.val):
                cur = cur.right
            elif(q.val < cur.val and p.val < cur.val):
                cur = cur.left
            else:
                return cur
      
        