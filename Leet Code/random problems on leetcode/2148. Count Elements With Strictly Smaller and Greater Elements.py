class Solution:
    def countElements(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            mn = min(nums)
            mx = max(nums)

            if(mn < nums[i] and mx > nums[i] ):
                cnt += 1
        return cnt
    