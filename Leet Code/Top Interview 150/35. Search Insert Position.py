class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] > target :
                    return i
            return(len(nums)+5)
                
a= Solution()
print(a.searchInsert([1,3,5,6], target = 10))