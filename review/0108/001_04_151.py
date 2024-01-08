class Solution:
    def solution(self, s):
        words = s.split()

        # 反转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        print(words)
        # 将列表转换成字符串
        return " ".join(words)


if __name__ == '__main__':
    Solution().solution(s="the sky is blue")
