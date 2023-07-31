class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j= len(nums)-1
        for i in range(k):
            nums.insert(0,nums[j])
            nums.pop(j+1)
            
        print(nums)

a=Solution()  # [5,6,7,1,2,3,4]
a.rotate(nums = [-1,-100,3,99], k = 2)

