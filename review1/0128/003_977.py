class Solution:
    def solution(self, nums):
        left = 0
        right = len(nums) - 1
        i = len(nums) - 1
        res = [float('inf')] * len(nums)  #
        while left < right:
            if pow(nums[left], 2) < pow(nums[right], 2):
                res[i] = pow(nums[right], 2)
                right -= 1
            elif pow(nums[left], 2) > pow(nums[right], 2):
                res[i] = pow(nums[left], 2)
                left += 1
            i -= 1
        print(res[1:])
        return nums


if __name__ == '__main__':
    Solution().solution(nums=[-4, -1, -1, 0, 3, 10])
