"""

例子
    77
"""


class Solution:
    def combine(self, n: int, k: int):
        result = []
        self.back(n, k, 1, [], result)

    def back(self, n, k, start_index, path, result):
        if len(path) == k:
            result.append(path[:])
        for i in range(start_index, n + 1):
            path.append(i)
            self.back(n, k, i + 1, path, result)
            path.pop() 
