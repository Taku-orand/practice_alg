from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i,numi in enumerate(nums):
      temp = target
      temp = temp - numi
      for j,numj in enumerate(nums):
        diff = temp-numj
        if i == j:
          continue
        if diff == 0:
          return [i,j]

a=Solution()
print(a.twoSum([3,2,4],6))