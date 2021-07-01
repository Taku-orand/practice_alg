from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def daq(left, right):
            if left == right:
                return nums[left]
            middle = (left + right) // 2
            leftNum = daq(left, middle)
            rightNum = daq(middle+1, right)
            resNum = calMax(left, right, middle)
            return max(leftNum, rightNum, resNum)

        def calMax(left, right, middle):
            leftSum = 0
            leftMax = float("-inf")
            for i in range(middle, left-1, -1):
                leftSum += nums[i]
                leftMax = max(leftMax, leftSum)
        
            rightSum = 0
            rightMax = float("-inf")
            for i in range(middle+1, right+1, 1):
                rightSum += nums[i]
                rightMax = max(rightSum, rightMax)
            return leftMax + rightMax
        return daq(0,len(nums)-1)
