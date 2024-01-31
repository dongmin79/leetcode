class Solution:
    def solution(self, nums, target=3):
        nums = sorted(nums)
        result = []
        for index, first_value in enumerate(nums):
            _left = index + 1
            _right = len(nums) - 1
            print(_left, _right)
            while _left < _right:
                _sum = nums[_left] + nums[_right] + first_value
                if _sum == target:
                    result.append([nums[index], nums[_left], nums[_right]])
                    break
                elif _sum < target:
                    _left += 1
                else:
                    _right -= 1
        return result


if __name__ == '__main__':
    print(Solution().solution(nums=[-1, 0, 1, 2, -1, -4]))
