# 非負の整数xが与えられたとき、xの平方根を計算して返します。

# 戻り値の型が整数であるため、10進数の桁は切り捨てられ、結果の整数部分のみが返されます。

# # 注意： pow(x, 0.5) や x ** 0.5 のような組み込みの指数関数や演算子を使用することはできません。
# import math
# class Solution:
#     def mySqrt(self, x: int) -> int:
#       return int(math.sqrt(x))
class Solution:
    def mySqrt(self, x: int) -> int:
      low = 1
      high = x
      if x < 2:
        return x
      while low < high:# sqrt < 4(low) < 5(right)これでもreturn midしなかったらlow−１にsqrtがあることになる
        mid = low + (high - low)//2
        if mid * mid == x:
          return mid
        elif mid * mid < x:# 9(mid*mid) < sqrt(10)
          low = mid + 1
        else:
          high = mid
      return low - 1

sol = Solution()
print(sol.mySqrt(5))
