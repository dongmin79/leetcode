# 后序遍历
from review import TreeNode


class Solution:
    def solution(self, root: TreeNode):
        if not root:
            return []
        left = self.solution(root.left)
        right = self.solution(root.right)
        return left + right + [root.value]

    def solution1(self, root: TreeNode):
        """
            5
            46
            1278
            后序 1247865
        """
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            current_node = stack.pop()
            result.append(current_node.value)
            if current_node.left:
                stack.append(current_node.right)
            if current_node.right:
                stack.append(current_node.left)
        return result[::-1]

    def solution3(self, root: TreeNode):
        """
        5
        46
        1278
        后序 1247865
        :param root:
        :return:
        """
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            current_node = stack.pop()
            if current_node is not None:
                stack.append(current_node)
                stack.append(None)
                if current_node.right:
                    stack.append(current_node.right)
                if current_node.left:
                    stack.append(current_node.left)
            else:
                current_node = stack.pop()
                result.append(current_node.value)
        return result
