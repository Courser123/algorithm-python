# https://leetcode-cn.com/problems/container-with-most-water/
from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        leftPt = 0
        rightPt = len(height) - 1
        max = 0
        while leftPt < rightPt:
            minHeight = min(height[leftPt], height[rightPt])
            area = minHeight * (rightPt - leftPt)
            if max < area:
                max = area

            if height[leftPt] == minHeight:
                leftPt += 1
            else:
                rightPt -= 1

        return max


test = Solution()

print(test.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
