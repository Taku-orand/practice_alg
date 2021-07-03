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
      space=False
      if len(s) == 0:
        return 0
      for c in s:
        if c != " ":
          if not space:
            i+=1
          else: 
            i=1
            space=False
        else:
          space=True
      return i

test = Solution()
print(test.lengthOfLastWord("a "))