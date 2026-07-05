# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # intialize list
        level_order_traversal = []
        # initialize queue
        q = collections.deque()
        # init queue with root node
        q.append(root)

        # start breadth first search while q is not empty
        # keep running until no nodes left in q
        while q:
            # get num of nodes in q (the length)
            # to iteratre thru 1 level at a time
            q_length = len(q)
            #init list to add nodes at each level
            level = []
            for i in range(q_length):
                # pop nodes from left of q
                # first in first out
                node = q.popleft()
                # check node not null
                if node:
                    # take node val and append to list level
                    level.append(node.val)
                    # add children of node to q
                    q.append(node.left)
                    q.append(node.right)
            # append level to trav list if level non empty
            if level:
                level_order_traversal.append(level)
        
        return level_order_traversal

        