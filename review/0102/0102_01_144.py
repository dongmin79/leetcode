# 前序遍历
from review import TreeNode


class Solution:
    def solution(self, root: TreeNode):
        if not root:
            return []
        left = self.solution(root.left)
        right = self.solution(root.right)
        return [root.value] + left + right

    def solution1(self, root: TreeNode):
        """
        5
        46
        1278
        前序 5412678
        :param root:
        :return:
        """
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            current_node = stack.pop()
            result.append(current_node.value)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
        return result

    def solution2(self, root: TreeNode):
        """
        5
        46
        1278
        前序 5412678
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
                if current_node.left:
                    stack.append(current_node.left)
                stack.append(current_node)
                stack.append(None)
            else:
                current_node = stack.pop()
                result.append(current_node.value)
        return result
