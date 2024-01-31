class Solution:
    def solution(self, nums, target=0):
        nums = sorted(nums)
        print(nums)
        result = []
        for index_1, first_value in enumerate(nums):
            for index_2, second_value in enumerate(nums[index_1 + 1:]):
                _left = index_1 + index_2 + 1 + 1
                _right = len(nums) - 1
                while _left < _right:
                    _sum = nums[_left] + nums[_right] + first_value + second_value
                    if _sum == target:
                        result.append([nums[index_1], nums[index_1 + 1:][index_2], nums[_left], nums[_right]])
                        break
                    elif _sum < target:
                        _left += 1
                    else:
                        _right -= 1
        return result


if __name__ == '__main__':
    print(Solution().solution(nums=[1, 0, -1, 0, -2, 2]))
