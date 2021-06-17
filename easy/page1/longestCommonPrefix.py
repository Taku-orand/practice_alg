from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      pre = 99999
      for i in range(0, len(strs)-1):
        j=0
        k=0
        count = 0
        while j < len(strs[i]) and k < len(strs[i+1]):
          if(strs[i][j] == strs[i+1][k]):
            count += 1
          else: break
          j += 1
          k += 1
        pre = min(pre, count)
      return strs[0][:pre]

test = Solution()
print(test.longestCommonPrefix(["flower","flow","flight"]))