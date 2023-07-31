class Solution:
    def removeElement(self, nums: list[int], val: int) :
        i=0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i=i-1
            i=i+1

        return len(nums) 
a = Solution()
print(a.removeElement( [3,2,2,3] , 3) )

'''
TypeError: (2, [2, 2]) is not valid value for the expected return type integer[]
    raise TypeError(str(ret) + " is not valid value for the expected return type integer[]");
Line 39 in _driver (Solution.py)
    _driver()
Line 46 in <module> (Solution.py)
During handling of the above exception, another exception occurred:
TypeError: slice indices must be integers or None or have an __index__ method
    out = ser._serialize(param_1[:ret], 'integer[]')
Line 36 in _driver (Solution.py)

'''