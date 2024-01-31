class Solution:
    def solution(self, nums, target):
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return -1


if __name__ == '__main__':
    print(Solution().solution(nums=[2, 7, 11, 15], target=14))
