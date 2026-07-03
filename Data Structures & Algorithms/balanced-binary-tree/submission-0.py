# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # dfs returns the height of the current subtree
        # if the subtree is unbalanced, return -1 as a warning signal
        def dfs(curr):
            # empty tree has height 0 and is balanced
            if not curr:
                return 0

            # get height of left subtree
            left = dfs(curr.left)
            if left == -1:
                return -1

            # get height of right subtree
            right = dfs(curr.right)
            if right == -1:
                return -1

            # if height difference is more than 1, not balanced
            if abs(left - right) > 1:
                return -1

            # otherwise return height of this subtree
            return max(left, right) + 1

        # tree is balanced if dfs does not return -1
        return dfs(root) != -1


        