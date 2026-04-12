# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       
        valide_nodes = 0

        def calculeValideN(root, max_node) :
            nonlocal valide_nodes

            if not root:
                return 

            if root.val >= max_node:
                valide_nodes += 1
                max_node = root.val
        
            
            calculeValideN(root.left, max_node)
            calculeValideN(root.right, max_node)
    

        calculeValideN(root, root.val)
        return valide_nodes