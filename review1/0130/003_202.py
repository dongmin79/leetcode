class Solution:
    def solution(self, s):
        result = []
        while True:
            nums = 0
            for i in str(s):
                nums += pow(int(i), 2)
            s = nums
            if s in result:
                return False
            else:
                result.append(s)
            if s == 1:
                return True
            print(result)

if __name__ == '__main__':
    Solution().solution(s=19)
