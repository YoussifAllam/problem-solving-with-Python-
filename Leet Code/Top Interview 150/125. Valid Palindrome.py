class Solution:
   def isPalindrome(self ,  s: str) -> bool:
    s = self.a(s)
    j=len(s)-1
    for i in range( (j // 2)+1 ):
        if i > j:
            break
        if not s[i] == s[j]:
            return False
        j-=1
        
    return True

   def a(self , s :str)-> str:
       n_s=''
       for i in range(len(s)):
           if s[i].isalnum() == True:
              n_s+= s[i].lower()

       return n_s
"0P"
a=Solution()
print(a.isPalindrome(s))