"""
快指针：寻找新数组的元素 ，新数组就是不含有目标元素的数组
慢指针：指向更新 新数组下标的位置
"""
from typing import List


class Solution:
    def solution(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
