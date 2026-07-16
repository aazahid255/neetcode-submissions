# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: binary tree
# output: number of good nodes in tree, meaning no nodes from the root to the current node that has a ndoe with a value greater
# edge cases: if root empty, return 0

# should do dfs 
# its path from root to the node, so we have to recruse from the root
# start from the root, and maintain a maximum
# we have a maximum as we go down both paths
# have a global counter
# if node is greater than the max so far, we set the max equal to that and set equal to the val of this node, keep recursing


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
     # this shouldnt be gloval
        self.good_nodes = 0

        def goodNodesCounter(root, max_val) -> int:
            if not root:
                return 0
            max_val = max(max_val, root.val)
            
            if root.val >= max_val:
                self.good_nodes += 1
            goodNodesCounter(root.left, max_val)
            goodNodesCounter(root.right, max_val)
    
        goodNodesCounter(root, -99999)
        return self.good_nodes



        