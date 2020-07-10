# https://leetcode-cn.com/problems/move-zeroes/
from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:

        return None

    def quickSort(self, nums: List[int], left: int, right: int) -> List[int]:

        if (left < right):

            baseNum = nums[left]
            begin = left
            end = right

            while begin < end:

                if nums[begin] < baseNum:
                    begin += 1

                elif nums[end] > baseNum:
                    end -= 1

                else:
                    temp = nums[begin]
                    nums[begin] = nums[end]
                    nums[end] = temp

            temp = baseNum
            baseNum = nums[end]
            nums[end] = temp

            self.quickSort(nums, left, begin - 1)
            self.quickSort(nums, begin + 1, right)

        return nums


test = Solution()

test.quickSort([0, 1, 0, 3, 12], 0, 4)
