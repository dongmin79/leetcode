# TODO 26、283、844、977
class Solution:
    def solution(self, nums, val):
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        print(nums)
        return slow


if __name__ == '__main__':
    Solution().solution(nums=[3, 2, 2, 3], val=3)
