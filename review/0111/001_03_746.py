class Solution:
    def solution(self, cost):
        dp = [0] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        print(dp)
        return dp[len(cost)]


if __name__ == '__main__':
    Solution().solution(cost=[10, 15, 20])
    Solution().solution(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
