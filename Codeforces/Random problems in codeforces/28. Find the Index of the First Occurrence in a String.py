class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenght = len(haystack)
        if needle in haystack:
            for i in range(lenght):
                if self.check( i , haystack , needle , lenght ) == True:
                    return i
        else:
            return -1


       
        
    def check(self,i ,haystack: str, needle: str ,lenght):
        for K  in range(len(needle)):
            for j in range( i , lenght ) :
                if needle[K] == haystack[j]:
                    i=i+1
                    break
                if needle[K] != haystack[j]:
                    return False
        return True


        
a= Solution()
print(a.strStr(haystack = "mississippi", needle = "issip") )

