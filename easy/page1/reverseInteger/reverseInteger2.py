class Solution:
  result = 0
  minusNum = False
  def reverse(self, x: int) -> int:
    if(x < 0):
      x = -x
      self.minusNum = True
    if x == 0:
      if (-2**31 <= self.result and self.result <= 2**31 -1) == False:
        return 0
      elif self.minusNum == True:
        self.result = -self.result
      return self.result
    temp = x % 10
    self.result = self.result*10 + temp
    x = x // 10
    return self.reverse(x)

test = Solution()
print(test.reverse(-2147483648))