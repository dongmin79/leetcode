class Solution:
    def helper(self, n, start_index, path, result):
        if start_index == len(n):
            result.append(path[:])
            return
        for i in range(start_index, len(n)):
            if self.is_hui_wen(n, start_index, i):
                path.append(n[start_index:i + 1])
                self.helper(n, i + 1, path, result)
                path.pop()

    def is_hui_wen(self, _str, start, end):
        i = start
        j = end
        while i < j:
            if _str[i] != _str[j]:
                return False
            i += 1
            j -= 1
        return True

    def solution(self, n):
        result = []
        self.helper(n, 0, [], result)
        print(result)
        return result


if __name__ == '__main__':
    Solution().solution("aab")
