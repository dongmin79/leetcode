class Solution:
    def solution(self, nums):
        left, right = 0, len(nums) - 1
        i = len(nums) - 1
        res = [0] * len(nums)
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                res[i] = pow(nums[right], 2)
                right -= 1
            else:
                res[i] = pow(nums[left], 2)
                left += 1
            i -= 1
        print(res)
        return res


if __name__ == '__main__':
    Solution().solution([-4, -1, 0, 3, 10])
