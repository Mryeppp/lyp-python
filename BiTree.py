# from LinkStack import LinkStack
class LinkNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkStack:
    def __init__(self):
        self.head = LinkNode()
        self.head.next = None

    def empty(self):
        if self.head.next == None:
            return True
        return False

    def push(self, e):
        p = LinkNode(e)
        p.next = self.head.next
        self.head.next = p

    def pop(self):
        assert self.head.next != None
        p = self.head.next;
        self.head.next = p.next
        return p.data

    def gettop(self):
        assert self.head.next != None
        return self.head.next.data


# from LinkQueue import LinkQueue
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkQueue(object):
    def __init__(self):
        self.front = None
        self.rear = None

    def clear(self):
        '''将队列置空'''
        self.front = None
        self.rear = None

    def isEmpty(self):
        '''判断队列是否为空'''
        return self.front is None

    def length(self):
        '''返回队列的数据元素个数'''
        p = self.front
        i = 0
        while p is not None:
            p = p.next
            i += 1
        return i

    def peek(self):
        '''返回队首元素'''
        if self.isEmpty():
            return None
        else:
            return self.front.data

    def offer(self, x):
        '''将数据元素x插入到队列成为队尾元素'''
        s = Node(x, None)
        if not self.isEmpty():
            self.rear.next = s
        else:
            self.front = s
        self.rear = s

    def poll(self):
        '''将队首元素删除并返回其值'''
        if self.isEmpty():
            return None
        p = self.front
        self.front = self.front.next
        if p == self.rear:  # 删除结点为队尾结点时需要修改rear
            self.rear = None
        return p.data

    def display(self):
        '''输出队列中的所有元素'''
        p = self.front
        while p is not None:
            print(p.data, end='')
            p = p.next


# 二叉链式存储结点类
class BiTreeNode(object):
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data  # 数据域的值
        self.lchild = lchild  # 左孩子的指针
        self.rchild = rchild  # 右孩子的指针


# 二叉树类
class BiTree(object):
    def __init__(self, root=None):
        self.root = root  # 二叉树的根节点

    # 依次输入先序序列创建二叉树
    def createBiTree(self, root):
        data = input('->')
        if data == '#':
            root = None
        else:
            root.data = data
            root.lchild = BiTreeNode()
            self.createBiTree(root.lchild)
            root.rchild = BiTreeNode()
            self.createBiTree(root.rchild)

    # 递归先序遍历
    def preOrder(self, root):
        if root is not None:
            self.VisitBTNode(root)
            self.preOrder(root.lchild)
            self.preOrder(root.rchild)

    # 递归中序遍历
    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.lchild)
            self.VisitBTNode(root)
            self.inOrder(root.rchild)

    # 递归后序遍历
    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.lchild)
            self.postOrder(root.rchild)
            self.VisitBTNode(root)

    # 遍历二叉树一个结点
    def VisitBTNode(self, BiTreeNode):
        # 值为#的结点代表空结点
        if BiTreeNode.data is not None:
            print(BiTreeNode.data, end=" ")

    # 队列实现层次遍历
    def order(self, root):
        q = LinkQueue()
        q.offer(root)
        while not q.isEmpty():
            p = q.poll()
            if p.data is not None:
                print(p.data, end=' ')
            if p.lchild is not None:
                q.offer(p.lchild)
            if p.rchild is not None:
                q.offer(p.rchild)


#####################################################
# 由先序序列创建二叉树
def createBiTree2():
    global ptr
    c = pre[ptr]
    if c != '#':
        root = BiTreeNode(c)
        ptr += 1
        root.lchild = createBiTree2()
        ptr += 1
        root.rchild = createBiTree2()
    else:
        root = None
    return root


# 非递归先序遍历
def preOrder2(root):
    p = root
    s = LinkStack()
    s.push(p)
    while not s.empty():
        p = s.pop()
        print(p.data, end=' ')
        while p is not None:
            if p.lchild is not None:
                print(p.lchild.data, end=' ')
            if p.rchild is not None:
                s.push(p.rchild)
            p = p.lchild


# 非递归中序遍历
def inOrder2(root):
    p = root
    s = LinkStack()

    while not s.empty() or p:
        while p:
            s.push(p)
            p = p.lchild
        if not s.empty():
            p = s.pop()
            print(p.data, end=' ')
            p = p.rchild


# 非递归后序遍历
def postOrder2(root):
    p = root
    t = None
    s = LinkStack()
    while not s.empty() or p:
        while p:
            s.push(p)
            p = p.lchild
        while not s.empty():
            p = s.gettop()
            if p.rchild == t or p.rchild is None:
                s.pop()
                print(p.data, end=' ')
                t = p
                if p == root:
                    return
            else:
                p = p.rchild
                break


#####################################################
# 二叉树上的查找算法
def searchNode(t, x):
    p = t
    if p is None:
        return None
    if p.data == x:
        return p
    else:
        lresult = searchNode(p.lchild, x)
    if lresult == None:
        return searchNode(p.rchild, x)
    else:
        return lresult


# 统计二叉树结点个数
def nodeCount(t):
    p = t
    count = 0
    if t is not None:
        count += 1
        count += nodeCount(p.lchild)
        count += nodeCount(p.rchild)
    return count


# 求二叉树的深度
def getDepth(t):
    p = t
    if p is None:
        return 0
    ldepth = getDepth(p.lchild)
    rdepth = getDepth(p.rchild)
    if ldepth < rdepth:
        return rdepth + 1
    else:
        return ldepth + 1


# 由中序和先序遍历序列建立二叉树
def createBiTree3(preOrder, inOrder, preo, ino, n):
    if n > 0:
        i = 0
        c = preOrder[preo]  # c为先序序列的根结点
        while i < n:
            if inOrder[i + ino] == c:
                break
            i += 1
        root = BiTreeNode(c)
        root.lchild = createBiTree3(preOrder, inOrder, preo + 1, ino, i)
        # 递归寻找左子树的根结点
        root.rchild = createBiTree3(preOrder, inOrder, preo + i + 1, ino + i + 1, n - i - 1)
        # 递归寻找右子树的根结点
        return root


'''test case

#input

A B C# #D E # # # G F # I # # H # #

# output

A B C D E G F I H
C B E D A F I G H
C E D B I F H G A
'''

if __name__ == '__main__':
    print("(1)依次输入先序序列创建二叉树：")
    print("A B C # # D E # # # G F # I # # H # # ")
    print("请仿照上述序列，每输入一个值按回车换行：")
    t = BiTreeNode()
    bT = BiTree()
    bT.createBiTree(t)
    print("(2)先序序列：")
    bT.preOrder(t)
    print("\n(3)中序序列：")
    bT.inOrder(t)
    print("\n(4)后序序列：")
    bT.postOrder(t)
    print("\n(5)层次序列：")
    bT.order(t)
    print("")
    #####################################################
    print("\n(6)一行输入先序序列创建二叉树：")
    print("A B C # # D E # # # G F # I # # H # # ")
    print("请仿照上述序列，输入一个先序序列：")
    pre = input().split(' ')
    ptr = 0
    t = createBiTree2()
    print("\n(7)非递归先序序列：")
    preOrder2(t)
    print("\n(8)非递归中序序列：")
    inOrder2(t)
    print("\n(9)非递归后序序列：")
    postOrder2(t)
    print()

    print("\n(10)在二叉树中查找 D：")
    x = "D"
    print(searchNode(t, x))
    print("\n(11)统计二叉树结点个数：", nodeCount(t))
    # print(nodeCount(t))
    print("\n(12)求二叉树的深度：", getDepth(t))
    # print(getDepth(t))
    #####################################################
    print("\n（13）由中序和先序遍历序列建立二叉树：")
    preOrder = "ABCDEGFIH"
    inOrder = "CBEDAFIGH"
    preo = 0
    ino = 0
    n = len(preOrder)
    t3 = createBiTree3(preOrder, inOrder, preo, ino, n)
    print("\n(14)先序、中序、后序遍历：")
    preOrder2(t3)
    print()
    inOrder2(t3)
    print()
    inOrder2(t3)
    print()
