# https://leetcode-cn.com/problems/move-zeroes/
from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:

        return self.move_zeros(nums)

    def move_zeros(self, nums: List[int]) -> List[int]:
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        for i in range(count, len(nums)):
            nums[i] = 0

        return nums


"""
    def move_zerosB(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] == 0:
                
        return []
"""
"""
    def move_zeros(self, nums: List[int]) -> List[int]:
        for num in nums:
            if num == 0:
                nums.append(num)
                nums.remove(num)

        return nums
"""

test = Solution()

print(test.moveZeroes([0, 1, 0, 3, 12]))
