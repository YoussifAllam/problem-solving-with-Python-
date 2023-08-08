# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    c =0
    def countNodes(self, root: TreeNode) -> int:
        def traversal(tree):
            if tree:
                    return 1+traversal(tree.left)+traversal(tree.right)
            return 0
            
        return traversal(root)

'''
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root:
            count += 1
            if root.left:
                count+= self.countNodes(root.left)
            if root.right:
                count += self.countNodes(root.right)
        return count
'''
         