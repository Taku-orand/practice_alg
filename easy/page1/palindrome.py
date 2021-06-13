class Solution:
    def isPalindrome(self, x: int) -> bool:
      givenNum = x
      reverse = 0
      if x < 0:
        return False
      while x != 0:
        reverse *= 10
        reverse = reverse + x % 10
        x //= 10
      if givenNum == reverse:
        return True
      else: return False

test = Solution()
print(test.isPalindrome(121))