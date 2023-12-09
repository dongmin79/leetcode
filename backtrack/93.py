# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#
#
#  例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
# 和 "192.168@1.1" 是 无效 IP 地址。
#
#
#  给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新
# 排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
#
#
#
#  示例 1：
#
#
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#
#
#  示例 2：
#
#
# 输入：s = "0000"
# 输出：["0.0.0.0"]
#
#
#  示例 3：
#
#
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 20
#  s 仅由数字组成
#
#
#  Related Topics 字符串 回溯 👍 1364 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.helper(s, 0, [], result)
        return result

    def helper(self, s, start_index, path, result):
        if start_index == len(s):
            if len(path) == 4:
                print(path)
            result.append(path)
        for i in range(start_index, len(s) + 1):
            if self.is_valid(s[start_index: i + 1]):
                path.append(s[start_index: i + 1])
                self.helper(s, i + 1, path, result)
                path.pop()

    def is_valid(self, s):
        if not 0 < len(s) < 4:
            return False
        if not 0 <= int(s) < 256:
            return False
        if len(s) > 1 and s.startswith("0"):
            return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # Solution().restoreIpAddresses("25525511135")
    Solution().restoreIpAddresses("010010")
