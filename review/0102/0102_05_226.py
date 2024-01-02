import collections

from review import TreeNode


class Solution:
    def solution(self, root: TreeNode):
        if not root:
            return root
        # root.left, root.right = root.right, root.left
        # self.solution(root.left)
        # self.solution(root.right)

        # self.solution(root.left)
        # root.left, root.right = root.right, root.left
        # self.solution(root.right)

        self.solution(root.left)
        self.solution(root.right)
        root.left, root.right = root.right, root.left
        return root

    def solution1(self, root: TreeNode):
        if not root:
            return None
        stack = [root]
        # while stack:
        #     current_node = stack.pop()
        #     current_node.left, current_node.right = current_node.right, current_node.left
        #     if current_node.left:
        #         stack.append(current_node.left)
        #     if current_node.right:
        #         stack.append(current_node.right)
        # while stack:
        #     current_node = stack.pop()
        #     if current_node.left:
        #         stack.append(current_node.left)
        #     current_node.left, current_node.right = current_node.right, current_node.left
        #     if current_node.left:
        #         stack.append(current_node.left)
        while stack:
            current_node = stack.pop()
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
            current_node.left, current_node.right = current_node.right, current_node.left
        return root

    def solution2(self, root: TreeNode):
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            for i in range(len(queue)):
                current_node = queue.popleft()
                current_node.left, current_node.right = current_node.right, current_node.left
                if current_node.left: queue.append(current_node.left)
                if current_node.right: queue.append(current_node.right)
        return root
