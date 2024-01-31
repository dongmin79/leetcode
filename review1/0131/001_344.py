class Solution:
    def solution(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)
        return s


if __name__ == '__main__':
    Solution().solution(s=["h", "e", "l", "l"])
