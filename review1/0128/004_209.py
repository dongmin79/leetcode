class Solution:
    def solution(self, nums, s):
        slow = 0
        fast = 0
        current_sum = 0
        current_len = float('inf')
        while fast < len(nums):
            current_sum += nums[fast]
            while current_sum >= s:
                current_len = min(current_len, fast - slow + 1)
                current_sum -= nums[slow]
                slow += 1
            fast += 1
        return current_len


if __name__ == '__main__':
    Solution().solution(nums=[2, 3, 1, 2, 4, 3], s=7)
