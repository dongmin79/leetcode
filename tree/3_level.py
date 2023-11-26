"""

队列先进先出，符合一层一层遍历的逻辑
栈先进后出适合模拟深度优先遍历也就是递归的逻辑

102.二叉树的层序遍历
107.二叉树的层次遍历II
199.二叉树的右视图
637.二叉树的层平均值
429.N叉树的层序遍历
515.在每个树行中找最大值
116.填充每个节点的下一个右侧节点指针
117.填充每个节点的下一个右侧节点指针II
104.二叉树的最大深度
111.二叉树的最小深度

"""
import collections

from tree import TreeNode


class Solution:

    def level_order(self, root: TreeNode):
        """长度 来遍历"""
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result

    def level(self, root: TreeNode):
        def helper(node, level, levels):
            if not node:
                return
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            helper(node.left, level + 1, levels)
            helper(node.right, level + 1, levels)

        levels = []
        helper(root, 0, levels)
        return levels
