class Solution:
    def reverse(self, x: int) -> int:
      result = 0
      minusNum = False
      if (-2**31 <= x and x <= 2**31 - 1) == False:
        return 0
      if x < 0:
        x = -x
        minusNum=True
      while x != 0:
        result *= 10
        temp = x % 10
        result += temp
        x = x // 10
      if minusNum:
        result = -result
      if (-2**31 <= result and result <= 2**31 - 1) == False:
        return 0
      return result

test= Solution()
print(test.reverse(2**31))