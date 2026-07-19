# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# input: 2 integer lists, preorder traversal and inorder traversal
# output: binary tree from the traverslas
# edge cases: empty lists

# match: dfs, tree traverslas

# plan:
# first node in pre order is always the root
# all the nodes before the root in the inorder traversal are in the left subtree
# all the nodes after the root in the inorder traversal are in the right subtree

# recursie solutoin
# if the lists dont exist, we just return nothing
# otherwie grab the root node form the preroder list [0]
# get its index from the inorder list, bc this will split the list in half
# create the left root by passing in the left side of preoder and left sdie of inorder
# do the same for the right side
# return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])
        return root
        
    
        