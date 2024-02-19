"""接雨水"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # res = 0
        # for index, value in enumerate(height[1:-1], start=1):
        #     left_max_height = height[index - 1]
        #     right_max_height = height[index + 1]
        #     for index_l, value_l in enumerate(height[:index], ):
        #         if value_l > left_max_height:
        #             left_max_height = max(value_l, left_max_height)
        #     for index_r, value_r in enumerate(height[index + 2:], start=index + 2):
        #         if value_r > right_max_height:
        #             right_max_height = max(value_r, right_max_height)
        #     res_ = min(left_max_height, right_max_height) - value
        #     print(value, left_max_height, right_max_height)
        #     if res_ > 0:
        #         res += res_
        # print(res)
        res = 0
        left_height = [0] * len(height)
        right_height = [0] * len(height)
        left_height[0] = height[0]

        for index, value in enumerate(height):
            left_height[index] = max(value, left_height[index - 1])
        right_height[-1] = height[-1]
        for index, value in enumerate(height[::-1]):
            right_height[index] = max(value, right_height[index - 1])
        right_height = right_height[::-1]
        result = 0
        for i in range(0, len(height)):
            summ = min(left_height[i], right_height[i]) - height[i]
            result += summ
        print(result)
        return res


#         12745
# 1 0 3
# 0 1 3
# 2 1 3
# 1 2 3
# 0 2 3
# 1 2 3
# 3 2 2
# 2 3 2
# 1 3 2
# 2 3 1
# [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
if __name__ == '__main__':
    height = [4, 2, 0, 3, 2, 5]
    # Solution().trap(height)
    Solution().solution(height)
# [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# [0] 0 0 1
# [0] 0 2 3
# [1, 0] 1 1 3
# [0] 0 5 6
# [1] 1 6 7
# [1, 0, 1] 1 4 7-
# [2, 1, 0, 1] 2 3 7
# [1] 1 9 10
