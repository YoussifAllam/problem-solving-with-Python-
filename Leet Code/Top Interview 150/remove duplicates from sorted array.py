class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        while i < len(nums):
            if nums.count(nums[i])>1:
                n = nums[i]
                nums.remove(n)
                i=i-1
            i =i+1

        res = sorted ( nums )
        return len(res)
    
a = Solution()
res = a.removeDuplicates( [1,1,2]) 
print( res )
