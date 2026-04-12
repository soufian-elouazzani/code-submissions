# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arbreL = []
        def arbre_to_list(root):
            if not root:
                return
            nonlocal arbreL 
            arbre_to_list(root.left)
            arbreL.append(root.val)
            arbre_to_list(root.right)
            return
        arbre_to_list(root)
        return arbreL[k-1]