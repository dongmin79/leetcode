"""
思路:
    1.确定递归函数的参数和返回值： 确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数， 并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型。
    2.确定终止条件： 写完了递归算法, 运行的时候，经常会遇到栈溢出的错误，就是没写终止条件或者终止条件写的不对，操作系统也是用一个栈的结构来保存每一层递归的信息，如果递归没有终止，操作系统的内存栈必然就会溢出。
    3.确定单层递归的逻辑： 确定每一层递归需要处理的信息。在这里也就会重复调用自己来实现递归的过程。
示例:
    144.二叉树的前序遍历(opens new window)
    145.二叉树的后序遍历(opens new window)
    94.二叉树的中序遍历
树:
    5
    46
    1278
    前序 5412678
    中序 1425768
    后序 1247865
"""
from tree import TreeNode


class Solution:
    def preorder_recursion(self, root: TreeNode):
        # 终止条件
        if not root:
            return []
        left = self.preorder_recursion(root.left)
        right = self.preorder_recursion(root.left)
        return [root.val] + left + right

    def inorder_recursion(self, root: TreeNode):
        if not root:
            return []
        left = self.preorder_recursion(root.left)
        right = self.preorder_recursion(root.left)
        return left + [root.val] + right

    def postorder_recursion(self, root: TreeNode):
        if not root:
            return []
        left = self.preorder_recursion(root.left)
        right = self.preorder_recursion(root.left)
        return left + right + [root.val]
