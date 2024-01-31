import math


class Solution:
    def solution(self, s, k=2):
        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)
        for cur in range(0, len(s), 2 * k):
            res[cur:cur + k] = reverse_substring(res[cur: cur + k])
        print(res)

if __name__ == '__main__':
    Solution().solution(s="abcde", k=3)
