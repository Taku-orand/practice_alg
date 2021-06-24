from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      length = len(nums) - 1
      left = 0
      right = length
      while(left <= right):
        middle = (left + right) // 2
        if nums[middle] == target:
          return middle
        elif nums[middle] > target:
          right = middle - 1
        else: left = middle + 1
      return left

test = Solution()
print(test.searchInsert([1,3,5,6], 0))