"""
树:
    5
    46
    1278
    前序 5412678
    中序 1425768
    后序 1247865

前序遍历
    -- 中左右
    根结点入栈、右孩子入栈、左孩子入栈
    出栈 -->

中序遍历
    左中右，
    先访问的是二叉树顶部的节点，
    然后一层一层向下访问，
    直到到达树左面的最底部，
    再开始处理节点（也就是在把节点的数值放进result数组中），

"""
from tree import TreeNode


class Solution:
    def preorder_iteration(self, root: TreeNode):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def inorder_iteration(self, root: TreeNode):
        if not root:
            return []
        stack = []
        result = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result

    def postorder_iteration(self, root: TreeNode):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result[::-1]

    def common_iteration(self, root: TreeNode):
        result = []
        st = []
        if root:
            st.append(root)
        # pre
        while st:
            node = st.pop()
            if node != None:
                if node.right:  # 右
                    st.append(node.right)
                if node.left:  # 左
                    st.append(node.left)
                st.append(node)  # 中
                st.append(None)
            else:
                node = st.pop()
                result.append(node.val)
        # in
        while st:
            node = st.pop()
            if node != None:
                if node.right:  # 添加右节点（空节点不入栈）
                    st.append(node.right)

                st.append(node)  # 添加中节点
                st.append(None)  # 中节点访问过，但是还没有处理，加入空节点做为标记。

                if node.left:  # 添加左节点（空节点不入栈）
                    st.append(node.left)
            else:  # 只有遇到空节点的时候，才将下一个节点放进结果集
                node = st.pop()  # 重新取出栈中元素
                result.append(node.val)  # 加入到结果集
        # post
        while st:
            node = st.pop()
            if node != None:
                st.append(node)  # 中
                st.append(None)

                if node.right:  # 右
                    st.append(node.right)
                if node.left:  # 左
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result
