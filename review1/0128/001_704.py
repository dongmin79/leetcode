class Solution:
    def solution(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            middle = left + (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return -1


if __name__ == '__main__':
    Solution().solution(nums=[-1, 0, 3, 5, 9, 12], target=9)
