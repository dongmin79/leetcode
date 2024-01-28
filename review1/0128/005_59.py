class Solution:
    def solution(self, n):
        nums = [[0] * n for _ in range(n)]
        start_x, start_y = 0, 0
        loop, mid = n // 2, n // 2
        count = 1
        for offset in range(1, loop + 1):
            print(offset)
            for i in range(start_y, n - offset):
                nums[start_x][i] = count
                count += 1
            print(nums)
            for i in range(start_x, n - offset):
                nums[i][n - offset] = count
                count += 1
            print(nums)

            for i in range(n - offset, start_y, -1):  # 从右至左
                nums[n - offset][i] = count
                count += 1
            print(nums)

            for i in range(n - offset, start_x, -1):  # 从下至上
                nums[i][start_y] = count
                count += 1
            print(nums)

            start_x += 1  # 更新起始点
            start_y += 1
        if n % 2 != 0:  # n为奇数时，填充中心点
            nums[mid][mid] = count
        print(nums)
        return nums

if __name__ == '__main__':
    Solution().solution(n=4)
