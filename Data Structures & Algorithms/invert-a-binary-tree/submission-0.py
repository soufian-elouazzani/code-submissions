# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return 
        # swap the two subtree that are related to the root
        placeholder = root.right
        root.right = root.left
        root.left = placeholder
        # make a recurcive call for each subtree
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)

        return root