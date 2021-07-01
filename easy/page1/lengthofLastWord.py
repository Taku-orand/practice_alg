# 文字列sがスペースで区切られたいくつかの単語で構成されている場合、
# 文字列の最後の単語の長さを返します。
# 最後の単語が存在しない場合は、0を返します。 
# 単語は、スペース以外の文字のみで構成される最大の部分文字列です。

# Example 1:
# Input: s = "Hello World"
# Output: 5

# Example 2:
# Input: s = " "
# Output: 0
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      i = 0
      if len(s) == 0:
        return 0
      rev = s[::-1]
      for c in rev:
        if c == " ":
          return i
        i += 1

test = Solution()
print(test.lengthOfLastWord(" a"))