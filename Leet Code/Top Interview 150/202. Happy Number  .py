class Solution:
    def isHappy(self, n: int) -> bool:
        n_num =0 
        n = str(n)
        #while n != '1' :
        for i in range(10):
           #print()
           for i in n :
               n_num += int(i)**2
               #print( n_num )

           n = str(n_num)
           n_num = 0
           if n == "1" : 
               return True
        return False
           
a = Solution()
print(a.isHappy( 2 ))
