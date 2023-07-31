class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = [p]
        queue2 = [q]
        while queue1 :
            getP = queue1.pop()
            getQ = queue2.pop()
            if (not getP and not getQ):
                    continue
            elif (not getP or not getQ):
                    return False
            elif getP.val == getQ.val:
                queue1.append(getP.left)
                queue1.append(getP.right)
                queue2.append(getQ.left)
                queue2.append(getQ.right)
            else:
               return False
        return True  
    
