# 中序遍历
from review import TreeNode


class Solution:
    def solution(self, root: TreeNode):
        if not root:
            return []
        left = self.solution(root.left)
        right = self.solution(root.right)
        return left + [root.value] + right

    def solution1(self, root: TreeNode):
        """
        5
        46
        1278
        中序 1425768
        :param root:
        :return:
        """
        result = []
        stack = []
        if not root:
            return result
        current_node = root
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                result.append(current_node.value)
                current_node = current_node.right
        return result

    def solution2(self, root: TreeNode):
        """
        5
        46
        1278
        中序 1425768
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
                if current_node.right:
                    stack.append(current_node.right)
                stack.append(current_node)
                stack.append(None)
                if current_node.left:
                    stack.append(current_node.left)
            else:
                current_node = stack.pop()
                result.append(current_node.value)
        return result
