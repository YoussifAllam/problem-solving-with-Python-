class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s=""
        for i in range(len(digits)):
            s+=str(digits[i])

        s=int(s)+1
        s=str(s)
        print(s)
        digits=[]

        for i in s:
            digits.append(int(i))
            
        return digits
    
a= Solution()
print(a.plusOne([9,9]))

