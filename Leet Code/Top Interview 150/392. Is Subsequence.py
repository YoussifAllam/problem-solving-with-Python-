class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length = len(t)
        index = 0
        for i in s:
           res , index = self.check( degit= i , index= index , length=length , t=t )
           if res == False:
               return False
        return True 
    
    def check( self , degit , index , length , t: str ) :
        for i in range(index , length ):
            if degit == t[i]:
                return True , i+1   
        return False , 0
            

a=Solution()
print(a.isSubsequence(s = "aaaaaa", t = "bbaaaa")) 
