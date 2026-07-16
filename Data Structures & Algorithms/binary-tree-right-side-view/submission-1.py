# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: root of a binary tree
# output: values of the nodes that are viisible from the ride side of tree, from TOP to bottom
# edge cases: empty nodes

# match: because we have to go from top to bottom, so this is definitely BFS. we are going level by level

# plan:
# this is the same as a level order traversal, we are just returning the last node in the level order
# so have a list initiated
# go through the root with a queue
# push the nodes at that level. once we have pushed all the nodes. we only want the most recent node, and add that to the list we initiated
# once queue is done, return the list


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        nodes = []
        queue = deque([root])
        while queue:
            length_list = len(queue)
            for i in range(length_list):
                node = queue.popleft()
                if i == length_list - 1:
                    nodes.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return nodes

        