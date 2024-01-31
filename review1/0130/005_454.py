class Solution:
    def solution(self, a, b, c, d):
        # 使用字典存储nums1和nums2中的元素及其和
        hashmap = dict()
        for n1 in a:
            for n2 in b:
                hashmap[n1 + n2] = hashmap.get(n1 + n2, 0) + 1

        # 如果 -(n1+n2) 存在于nums3和nums4, 存入结果
        count = 0
        for n3 in c:
            for n4 in d:
                key = - n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count


if __name__ == '__main__':
    Solution().solution(a=[1, 2], b=[-2, -1], c=[-1, 2], d=[0, 2])
