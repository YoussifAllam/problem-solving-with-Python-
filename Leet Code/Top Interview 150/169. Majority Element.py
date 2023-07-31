class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        conuter = 0
        number = 0
        checked=[]
        for i in range(len(nums)):
            if  nums[i]  in checked:
                continue
            n_c  = nums.count(nums[i])
            if n_c > conuter:
                checked.append(nums[i])
                conuter = n_c
                number = nums[i]

        return number
    
a= Solution()
print(a.majorityElement( nums = [3,3,4] ) )

