class Solution:

    def backtracking(self, n, k, start_index, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start_index, n + 1):
        # for i in range(start_index, n - (k - len(path)) + 2):  # 优化的地方
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()

    def solution(self, _n, _k):
        result = []
        self.backtracking(n, k, 1, [], result)
        return result


if __name__ == '__main__':
    n = 4
    k = 2
    Solution().solution(n, k)
