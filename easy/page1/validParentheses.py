class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      res = False
      for i in range(len(s)):
        if s[i] in ["(", "{", "["]:
          stack.append(s[i])
        elif(s[i] in [")", "}", "]"]): 
          if(len(stack) == 0):
            return False
          if([")", "}", "]"].index(s[i]) != ["(", "{", "["].index(stack.pop())):
            return False
      if(len(stack)  == 0):
         res = True
      return res

test = Solution()
print(test.isValid("{[]}"))