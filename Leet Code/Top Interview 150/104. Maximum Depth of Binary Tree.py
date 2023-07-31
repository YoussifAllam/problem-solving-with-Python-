# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''
            def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
            
        return res
        '''
        root = TreeNode()
        if root is None:
            return 0
        queue = [root]
        vasited = []
        depth = 1
        
        while queue:
            node  = queue.pop()

            if node in vasited:
               continue
            vasited.append(node)

            if node.left != None and node.right != None:
                queue.append(node.left)
                queue.append(node.right)
                depth+=1

            elif node.right != None:
                queue.append(node.right)
                depth+=1

            elif node.left != None:
                queue.append(node.left)
                depth+=1

        return depth


