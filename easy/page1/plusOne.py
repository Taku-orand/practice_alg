# 非負の整数を表す10進数の空でない配列が与えられたとき、その整数を1つ増やしてください。

# 桁は、最上位の桁がリストの先頭に来るように格納されており、配列の各要素には1つの桁が含まれています。

# 整数の先頭には0が含まれていないと仮定することができますが、数字の0自体は除きます。
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      if digits[-1] != 9:
        digits[-1] += 1
      else:
        n = -len(digits)
        i= -1
        while i>=n:
          if digits[i] == 9:
            digits[i] = 0
          else:
            break
          i -= 1
        if i>=n:
          digits[i] += 1
        else:
            digits = [1] + [0]*len(digits)
      return digits
        

test = Solution()
print(test.plusOne([8,9,9,9]))