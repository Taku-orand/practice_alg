# 2つのバイナリ文字列aとbが与えられると、それらの合計をバイナリ文字列として返します。
class Solution:
    def addBinary(self, a: str, b: str) -> str:
      a_bi = int('0b'+a,2)
      b_bi = int('0b'+b,2)
      res = bin(a_bi+b_bi)
      return res[2:]

sol = Solution()
print(sol.addBinary("11","1"))