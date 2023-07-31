class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        length = len( nums )
        if length == 0 : return[]
        if length == 1 : return [f"{nums[0]}" ]
        
        interval =[]
        end = nums [length-1]
        start = nums[0]

        for i in range( 1 , length ) :
            curr = nums[i]  # 6
            last = nums[i-1] # 4
            if i == 0  or curr - last != 1:
               if start == last :
                   interval.append( f"{start}")
               else:
                  interval.append( f"{start}->{last}")
               start = nums[i]

            if start == end :
                interval.append( f"{start}")

            elif  i == length-1 :
                   interval.append( f"{start}->{end}")
                   break
               
        return interval
a = Solution()
print( a.summaryRanges( nums = [-1]) )

'''
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

'''
