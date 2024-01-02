# 层序遍历 TODO(107、199、637、429、515、116、117、104、111)
import collections

from review import TreeNode


class Solution:
    def solution(self, root: TreeNode):
        """
        6
        47
        1358
        :param root:
        :return:
        """
        result = []
        if not root:
            return result
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                current_node = queue.popleft()
                level.append(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(level)
        return result

    def helper(self, current_node, level, levels):
        if not current_node:
            return
        if len(levels) == level:
            levels.append([])
        levels[level].append(current_node.value)
        self.helper(current_node.left, level + 1, levels)
        self.helper(current_node.right, level + 1, levels)

    def solution1(self, root: TreeNode):
        levels = []
        self.helper(root, 0, levels)
        return levels
