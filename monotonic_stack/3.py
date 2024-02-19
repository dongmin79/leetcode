class Solution:
    def solution1(self, nums1, nums2):
        res = []
        stack = []
        num_map = dict()
        for index, value in enumerate(nums2):
            while stack and stack[-1] < value:
                num_map[stack[-1]] = value
                stack.pop()
            stack.append(index)
        print(num_map)



if __name__ == '__main__':
    # Solution().solution1(nums1=[4, 1, 2], nums2=[1, 3, 4, 2, 5])
    Solution().solution(nums1=[73, 74, 75, 71, 69, 72, 76, 73])
