# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# height = 1 + max(left, right)
# diameter = left + right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # intialize diameter result counter
        self.res = 0

        # returns height
        def dfs(curr):
            """
            - computes the height of the subtree
            - updates the maximum diameter
            """
            # if empty, abse case
            if not curr:
                return 0
            
            # height of left subtree
            left = dfs(curr.left)
            #height of right 
            right = dfs(curr.right)

            # compare max of result with current diameter (left + right height)
            self.res = max(self.res, left + right)
            # return height + 1 (1 is the current node we are at)
            # max of height from curr
            return max(left,right) + 1 
        #call recursive function from root
        dfs(root)
        return self.res
        

        

        