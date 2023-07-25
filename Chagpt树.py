class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BiTree:
    def __init__(self, root=None):
        self.root = root

    # 递归创建二叉树
    def create(self, values, i):
        if i >= len(values) or values[i] == '#':
            return None
        node = BiTreeNode(values[i])
        node.lchild = self.create(values, 2 * i + 1)
        node.rchild = self.create(values, 2 * i + 2)
        return node

    # 先序遍历二叉树
    def pre_order_traversal(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.pre_order_traversal(root.lchild)
        self.pre_order_traversal(root.rchild)

    # 非递归先序遍历
    def pre_order_traversal_no_recursion(self, root):
        if root is None:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            print(node.data, end=' ')
            if node.rchild:
                stack.append(node.rchild)
            if node.lchild:
                stack.append(node.lchild)

    # 中序遍历二叉树
    def in_order_traversal(self, root):
        if root is None:
            return
        self.in_order_traversal(root.lchild)
        print(root.data, end=' ')
        self.in_order_traversal(root.rchild)

    # 非递归中序遍历
    def in_order_traversal_no_recursion(self, root):
        if root is None:
            return
        stack, node = [], root
        while stack or node:
            if node:
                stack.append(node)
                node = node.lchild
            else:
                node = stack.pop()
                print(node.data, end=' ')
                node = node.rchild

    # 后序遍历二叉树
    def post_order_traversal(self, root):
        if root is None:
            return
        self.post_order_traversal(root.lchild)
        self.post_order_traversal(root.rchild)
        print(root.data, end=' ')

    # 非递归后序遍历
    def post_order_traversal_no_recursion(self, root):
        if root is None:
            return
        stack1, stack2 = [root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.lchild:
                stack1.append(node.lchild)
            if node.rchild:
                stack1.append(node.rchild)
        while stack2:
            node = stack2.pop()
            print(node.data, end=' ')

    # 层次遍历二叉树
    def level_order_traversal(self, root):
        if root is None:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    # 在二叉树中查找 D，返回结点
    def find_node(self, root, data):
        if root is None:
            return None
        if root.data == data:
            return root
        node = self.find_node(root.lchild, data)
        if node is not None:
            return node
        return self.find_node(root.rchild, data)

    # 统计二叉树结点个数
    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.lchild) + self.count_nodes(root.rchild)

    # 求二叉树深度
    def depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.depth(root.lchild), self.depth(root.rchild))

    # 由中序和先序遍历序列建立二叉树
    def build_tree(self, inorder, preorder):
        if not inorder or not preorder:
            return None
        root_value = preorder[0]
        root = BiTreeNode(root_value)
        i = inorder.index(root_value)
        root.lchild = self.build_tree(inorder[:i], preorder[1:i+1])
        root.rchild = self.build_tree(inorder[i+1:], preorder[i+1:])
        return root

if __name__ == '__main__':
    pass