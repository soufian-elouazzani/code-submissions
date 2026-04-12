# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
                return None

        rootNode = TreeNode(preorder[0])

        index = inorder.index(rootNode.val)
        

        rootNode.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        rootNode.right = self.buildTree(preorder[index+1::], inorder[index+1::])

        return rootNode
            
            
