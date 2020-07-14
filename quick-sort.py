from typing import List


class Solution:

    def quickSort(self, nums: List[int], begin: int, end: int) -> List[int]:

        if (begin < end):

            key = nums[begin]
            left = begin
            right = end

            while left < right:

                while left < right and nums[right] >= key:
                    right -= 1

                nums[left] = nums[right]

                while left < right and nums[left] < key:
                    left += 1

                nums[right] = nums[left]

            nums[left] = key

            self.quickSort(nums, begin, left - 1)
            self.quickSort(nums, left + 1, end)

        return nums

    def quick_sort(self, array: List[int], left: int, right: int):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right] > key:
                right -= 1
            array[left] = array[right]
            while left < right and array[left] <= key:
                left += 1
            array[right] = array[left]
        array[right] = key
        self.quick_sort(array, low, left - 1)
        self.quick_sort(array, left + 1, high)
