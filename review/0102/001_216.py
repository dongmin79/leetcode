class Solution:
    def solution(self, k, n, ):
        result = []
        self.helper(n, k, 1, [], result)
        print(result)
        return result

    def helper(self, k, n, start_index, path, result):
        if sum(path) > k:
            return
        if len(path) == n:
            if sum(path) == k:
                result.append(path[:])
            return
        for i in range(start_index, 9 - (n - len(path)) + 2):
            path.append(i)
            self.helper(k, n, i + 1, path, result)
            path.pop()


if __name__ == '__main__':
    Solution().solution(k=3, n=9)
