class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) > 0:
            j=0
            for i in range(m+n):
                if nums1[i] == 0:
                    nums1[i] = nums2[j]
                    j+=1
                    if j > len(nums2)-1:
                        break

        nums1.sort()


a =Solution()
a.merge(nums1 = [-1,0,0,3,3,3,0,0,0] , m = 6 , nums2 = [1,2,2] , n = 3 )
