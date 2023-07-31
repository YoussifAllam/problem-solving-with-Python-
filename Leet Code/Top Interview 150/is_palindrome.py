class Solution:
  def is_palindrome(self , x):
    if x < 0:
        return False
    
    # reverse the integer
    rev = 0
    temp = x
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    
    # check if the reversed integer is equal to the original integer
    return rev == x

if __name__ == "__main__":
    a = Solution()
    target = int(input())
    print( a.is_palindrome(target) )