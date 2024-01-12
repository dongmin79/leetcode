class Solution:
    def solution(self, n: int):
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            print(i, i - 1, i - 2, dp)
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        return dp[n]


if __name__ == '__main__':
    print(Solution().solution(n=10))
