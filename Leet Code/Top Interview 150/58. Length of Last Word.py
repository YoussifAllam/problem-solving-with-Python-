class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        #? print(s)
        return len(s[-1])
    
    
a=Solution()
print(a.lengthOfLastWord("   fly me   to   the moon  "))
