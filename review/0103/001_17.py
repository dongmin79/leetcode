class Solution:
    def __init__(self):
        self.map = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
        }

    def helper(self, n, k, start_index, path, result):
        if len(path) == k:
            result.append(''.join(path[:]))
            return
        for value in self.map[n[start_index]]:
            path.append(value)
            self.helper(n, k, start_index + 1, path, result)
            path.pop()

    def solution(self, n):
        result = []
        self.helper(n, len(n), 0, [], result)
        print(result)
        return result


if __name__ == '__main__':
    Solution().solution("23")
