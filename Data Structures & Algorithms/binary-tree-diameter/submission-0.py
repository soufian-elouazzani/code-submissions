# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        def depthNode(root: Optional[TreeNode]):
            if not root :
                return 0
            return 1 + max(depthNode(root.left), depthNode(root.right))

        current_Mhight = depthNode(root.left) + depthNode(root.right)
        
        current_Mhight = max (self.diameterOfBinaryTree(root.left), current_Mhight)
        current_Mhight = max (self.diameterOfBinaryTree(root.right), current_Mhight)
        
        return current_Mhight
