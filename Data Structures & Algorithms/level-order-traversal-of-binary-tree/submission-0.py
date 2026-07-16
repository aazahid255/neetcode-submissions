# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# input: tree
# output: nested list, level order traversal of the tree
# edge cases: empty tree, only one level

# match: queue, tree


# have a queue for current nodes and their children
# have a list for nodes (what we return in the end)
# have a lsit taht represents the level we are currently visiting
# we add the current nodes to nodes list
# then, we traverse the current nodes and add all their children to a temp list
# then, we clear the original list we added to nodes and make it equal to their chilren
# clear the temp list
# repeat until queue is empty

# preoder
# visit node
# postoder

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        while queue:
            length_level = len(queue)
            current_level_nodes = []
            for _ in range(length_level):
                node = queue.popleft()
                current_level_nodes.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(current_level_nodes)
        return result

            


        