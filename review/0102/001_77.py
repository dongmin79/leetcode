class Solution:
    def helper(self, n, k, start_index, path, result):
        if len(path) == k:
            result.append(path[:])
        # for i in range(start_index, n + 1):
        for i in range(start_index, n - (k - len(path)) + 2):
            path.append(i)
            self.helper(n, k, i + 1, path, result)
            path.pop()

    def solution(self, n, k):
        result = []
        self.helper(n, k, 1, [], result)
        return result


if __name__ == '__main__':
    Solution().solution(n=4, k=2)
