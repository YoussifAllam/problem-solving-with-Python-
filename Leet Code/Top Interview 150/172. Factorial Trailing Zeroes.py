class Solution:  
    def trailingZeroes(self,n):
        count = 0
        while(n >= 5):
            n //= 5
            count += n
    
        return count
                
o = Solution()
print(o.trailingZeroesa(10))

