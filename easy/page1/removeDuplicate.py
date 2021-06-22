from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      j=0
      for i in range(len(nums)):
        if nums[j] < nums[i]:
            j += 1
            nums[j] = nums[i]
      return j + 1

test = Solution()
print(test.removeDuplicates([1,1,2]))