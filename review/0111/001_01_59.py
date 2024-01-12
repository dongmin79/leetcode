class Solution:
    def solution(self, n: int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.solution(n - 1) + self.solution(n - 2)
        # 0 0
        # 1 1
        # 2 1
        # 3 2

    def solution1(self, n: int):
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            print(i,i-1,i-2,dp)
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        return dp[n]


if __name__ == '__main__':
    print(Solution().solution(n=4))
    print(Solution().solution1(n=10))
