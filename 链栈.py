class LinkedListStackNode:

    def __init__(self, data=None,next=None):
        """初始化链栈结点
        :param data: 链栈结点的数据
        """
        self.data = data
        self.next = next


class LinkedListStack:
    """链栈
    """

    def __init__(self):
        """初始化链栈
        """
        self.top = LinkedListStackNode(None)

    def IsEmptyStack(self):
        """判断栈是否为空
        :return: 空True 非空False
        """
        return self.top is None

    def GetTopStack(self):
        """获取链栈顶数据
        :return self.top.next.data: 栈顶数据
        """
        if self.IsEmptyStack():
            print("栈空！")
            return
        else:
            return self.top.next.data

    def StackTraverse(self):
        """遍历链栈
        """
        if self.IsEmptyStack():
            print("栈空！")
            return
        cursorNode = self.top.next
        print("当前栈顶至栈底数据为：")
        while cursorNode != None:
            print(cursorNode.data)
            cursorNode = cursorNode.next
            if cursorNode == None:
                print("------栈底")
            else:
                print("↓")


    def GetStackLength(self):
        """获取当前栈长度
        :return count:栈长度
        """
        count = 0
        if self.IsEmptyStack():
            print("栈空！")
            return
        cursorNode = self.top.next
        while cursorNode != None:
            count += 1
            cursorNode = cursorNode.next
        return count

    def PushStack(self, element):
        """入栈
        """
        newStackNode = LinkedListStackNode(element)
        newStackNode.next = self.top.next #链表：前指向后
        self.top.next = newStackNode

    def PopStack(self):
        """出栈
        :return data: 出栈数据
        """
        if self.IsEmptyStack():
            print("栈空！")
            return
        else:
            removedStackNode = self.top
            self.top=self.top.next
            return removedStackNode.data

    def CreateStackByInput(self):
        """创建链栈
        """
        data = input("请输入栈顶数据，按#结束：")
        while data != '#':
            self.PushStack(data)
            data = input("请输入栈顶数据，按#结束：")
        self.StackTraverse()


ls = LinkedListStack()
print(ls.IsEmptyStack())
ls.CreateStackByInput()
data = input("输入入栈数据：")
ls.PushStack(data)
ls.StackTraverse()
print(ls.GetStackLength())

