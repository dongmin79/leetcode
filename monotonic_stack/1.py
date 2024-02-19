from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [0]
        for index, value in enumerate(temperatures[1:], start=1):
            if value <= temperatures[stack[-1]]:
                stack.append(index)
            else:
                while stack and temperatures[stack[-1]] <= value:
                    answer[stack[-1]] = index - stack[-1]
                    stack.pop()
                stack.append(index)
        print(answer)

    def solution(self, nums1):
        res = [0] * len(nums1)
        stack = []
        num_map = dict()
        for index, value in enumerate(nums1):
            while stack and nums1[stack[-1]] < value:
                num_map[stack[-1]] = index
                stack.pop()
            stack.append(index)
        for key, value in num_map.items():
            print(key, value)
            res[key] = value - key
        print(res)


if __name__ == '__main__':
    Solution().dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])
