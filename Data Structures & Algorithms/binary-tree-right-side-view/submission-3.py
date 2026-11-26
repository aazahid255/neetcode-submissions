# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: root of binary tree
# output: list of integers, it is the array of all right side binary tree
# edge cases: root empty, only one root in tree, return [] and [root]

# inorder traversla using queue, only return end of queue to our list

# initialize a queue with root inside it
# intiialse a result array
# while queue loop
# get length of queue
# iterate in a loop gets the value of current node, adds its cxhildren, and pops current node
# once we hvae iterated through this, we shudl have value of the last node in the level. add thsi to our output array.
# after queue is empty, we return the output array

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([root])
        output = []
        while queue:
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)
            output.append(cur_node.val)
        return output

        