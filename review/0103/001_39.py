class Solution:
    def helper(self, n, target, start_index, path, result):
        if sum(path) > target:
            return
        if sum(path) == target:
            result.append(path[:])
            return
        for i in range(start_index, len(n)):
            path.append(n[i])
            self.helper(n, target, i, path, result)
            path.pop()

    def solution(self, n, target):
        result = []
        self.helper(n, target, 0, [], result)
        print(result)
        return result
        pass


if __name__ == '__main__':
    Solution().solution([2, 3, 6, 7], 7)
