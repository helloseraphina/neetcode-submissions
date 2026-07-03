# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subroot is empty it is still a subroot
        if not subRoot:
            return True
        # if root is empty, it cannot be root of a subroot
        if not root:
            return False
        
        if self.isSametree(root, subRoot):
            return True
        
        # check if subroot to left and right tree of root
        return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
    def isSametree(self, root, subroot):
        if not root and not subroot:
            return True

        if root and subroot and root.val == subroot.val:
            return (self.isSametree(root.left, subroot.left) and self.isSametree(root.right, subroot.right))
        
        #if not root or not subroot:
        return False
        