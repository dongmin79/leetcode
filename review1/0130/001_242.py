class Solution:
    def solution(self, s, t):
        # 若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

        record = [0] * 26
        for i in s:
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] += 1

        for i in range(26):
            if record[i] != 0:
                return False
        return True


if __name__ == '__main__':
    Solution.solution(s="anagram", t="nagaram")
