# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# the absolute smallest node ( k = 1) is in the node all the way to the left. 
# lets recruse all the way to the left. 
# keep a count k. when we go all the way to the left, count is equal to 1
# if not root.left, we have hit the smallest node in the bst
# atp, set count = 1
# set count = 1. then recurse 

# what if we just added all nodes to a list?
# lets recurse to the left, then we keep recursing backward until we are done


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.k = k
        self.val = -1
        def inorder_recursive(root):
            if root is None or self.val is not -1:
                return
            inorder_recursive(root.left) 
            self.count += 1
            if self.count == self.k:
                self.val = root.val
                return
            inorder_recursive(root.right)
        inorder_recursive(root)
        return self.val

            
        
