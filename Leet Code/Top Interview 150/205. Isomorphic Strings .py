class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len (s) != len(t):
            return False
        hash = {}
        for i in range(len(s)):
            if s[i] in hash.keys():
                #print(hash ,"\n")
                if hash[ s[i] ] != t[i]  :
                    return False
            else:
                if t[i]  in hash.values():
                    return False
                hash[s[i]] = t[i]
                
        return True
a = Solution()
print(a.isIsomorphic(  s = "paper", t = "title" ))
