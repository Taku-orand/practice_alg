class Solution:
    def climbStairs(self, n: int) -> int:
      memo = [0 for _ in range(n)]
      return self.rec(0,n,memo)
    def rec(self,i,n,memo):
      if i > n:
        return 0
      if i == n:
        return 1
      if (memo[i]>0):
        return memo[i]
      memo[i] = self.rec(i+1,n,memo) + self.rec(i+2,n,memo)
      return memo[i]

sol = Solution()
print(sol.climbStairs(4))