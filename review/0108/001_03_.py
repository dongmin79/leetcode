class Solution:
    def solution(self, s, s1):
        _count = 0
        for _ in s:
            if _.isdigit():
                _count += 1
        result = ["a"] * (len(s) + _count * len(s1))
        print(result)
        fast = 0
        slow = 0
        while fast < len(s):
            if not s[fast].isdigit():
                slow += 1
                result[slow] = s[fast]
            else:
                for _ in s1:
                    result[slow] = _
                    slow += 1
            fast += 1
        print(result)

if __name__ == '__main__':
    Solution().solution(s="a1b2c3", s1="number")
