class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if (ln := len(nums)) == len(set(nums)):
            return False
        Hash = {}
        for i in range(len(nums)):
            digit = nums[i]
            if digit in Hash and abs( Hash.get(digit) - i ) <=  k :
                return True 
            else:
                Hash[digit] = i
        return False
 



a = Solution()
print(a.containsNearbyDuplicate( nums = [1,2,3,1,1,2,3], k = 2 ))
                    #                    0 1 2 3 4 5