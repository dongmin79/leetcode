class Solution:
    def solution(self, n, k):
        result = []
        n.sort()
        self.helper(n, k, 0, [], result)
        print(result)
        return result

    def helper(self, n, k, start_index, path, result):
        if sum(path) > k:
            return
        if sum(path) == k:
            result.append(path[:])
            return
        for i in range(start_index, len(n)):
            if i > start_index and n[i] == n[i - 1]:
                continue
            path.append(n[i])
            self.helper(n, k, i + 1, path, result)
            path.pop()


if __name__ == '__main__':
    Solution().solution([10, 1, 2, 7, 6, 1, 5], 8)
