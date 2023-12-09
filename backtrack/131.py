# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
#  回文串 是正着读和反着读都一样的字符串。
#
#
#
#  示例 1：
#
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#
#
#  示例 2：
#
#
# 输入：s = "a"
# 输出：[["a"]]
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 16
#  s 仅由小写英文字母组成
#
#
#  Related Topics 字符串 动态规划 回溯 👍 1695 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.helper(s, 0, [], result)
        print(result)
        return result

    def helper(self, s, start_index, path, result):
        if start_index == len(s):
            result.append(path[:])
        for i in range(start_index, len(s)):
            if self.is_palindrome(s, start_index, i):
                path.append(s[start_index:i + 1])
                self.helper(s, i + 1, path, result)
                path.pop()

    def is_palindrome(self, s, start, end):
        i, j = start, end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    Solution().partition("aab")
