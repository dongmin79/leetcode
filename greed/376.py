class Solution:
    def solution(self, _data):
        result = 1
        current_diff = 0
        pre_diff = 0
        for index, value in enumerate(_data[:-1]):
            current_diff = _data[index + 1] - value
            print(current_diff)
            if any(
                    [
                        current_diff > 0 and pre_diff <= 0,
                        current_diff < 0 and pre_diff >= 0,
                    ]
            ):
                print(1, current_diff, value)
                result += 1
                pre_diff = current_diff
        print(result)
        return result

    def wiggleMaxLength(self, nums) -> int:
        # 0 i 作为波峰的最大长度
        # 1 i 作为波谷的最大长度
        # dp是一个列表，列表中每个元素是长度为 2 的列表
        dp = []
        for i in range(len(nums)):
            # 初始为[1, 1]
            dp.append([1, 1])
            for j in range(i):
                # nums[i] 为波谷
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                # nums[i] 为波峰
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        print(dp)
        return max(dp[-1][0], dp[-1][1])


if __name__ == '__main__':
    data = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    Solution().solution(data)
    Solution().wiggleMaxLength(data)
