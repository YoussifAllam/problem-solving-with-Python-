class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
      l = 0
      r = len(numbers)-1
      while l < r:
        #sum = numbers[l] + numbers[r]
        if numbers[l] + numbers[r] < target:
            l+=1
        elif numbers[l] + numbers[r] > target:
            r-=1
        else:            
            return [l+1 , r+1]
        
a=Solution()
print(a.twoSum( [2,7,11,15] , target=9 ) )



  