from numpy import sqrt 
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))
    
a=Solution()
print(a.mySqrt(8))