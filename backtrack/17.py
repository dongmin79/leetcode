# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#
#
#  示例 1：
#
#
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
#  示例 2：
#
#
# 输入：digits = ""
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：digits = "2"
# 输出：["a","b","c"]
#
#
#
#
#  提示：
#
#
#  0 <= digits.length <= 4
#  digits[i] 是范围 ['2', '9'] 的一个数字。
#
#
#  Related Topics 哈希表 字符串 回溯 👍 2697 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def __init__(self):
        self.map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        current_index = 0

        self.helper(digits, current_index, [], result)
        print(result)
        return result

    def helper(self, digits, current_index, path, result):
        if current_index == len(digits):
            result.append(''.join(path))
            return
        for current_value in self.map[digits[current_index]]:
            path.append(current_value)
            self.helper(digits, current_index + 1, path, result)
            path.pop()


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    Solution().letterCombinations("24")
