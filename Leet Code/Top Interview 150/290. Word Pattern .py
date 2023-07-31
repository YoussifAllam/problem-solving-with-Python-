class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len (s) != len(pattern):
            return False
        Hash = {}
        for i in range (len( pattern ) ):
            #if pattern[i] in Hash.keys():
            if Hash.get(pattern[i]) != None :
                if s[i] != Hash.get( [pattern[i]] ) : 
                    return False
            else:
                #if s[i] in Hash.values():
                if Hash.get(s[i]) != None :
                    return False
                Hash[pattern[i]] = s[i]
        return True 

a = Solution()
print(a.wordPattern( pattern = "ab", s=  "happy hacking" ))

