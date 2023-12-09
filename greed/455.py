"""
大饼干优先
    遍历孩子找饼干
小饼干优先
    遍历饼干找孩子
"""


class Solution:
    def solution(self, g, s):
        g.sort()  # 将孩子的贪心因子排序
        s.sort()  # 将饼干的尺寸排序
        index = len(s) - 1
        result = 0
        for i in range(len(g) - 1, -1, -1):
            if index >= 0 and s[index] >= g[i]:
                result += 1
                index -= 1
        return result

        # index = 0
        # for i in range(len(s)):
        #     if index < len(g) and g[index] <= s[i]:
        #         index += 1
        # return index
