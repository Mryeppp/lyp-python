
from abc import ABCMeta, abstractmethod, abstractproperty


class IList(metaclass=ABCMeta):
    @abstractmethod
    def clear(self):
        '''将线性表置成空表'''
        pass

    def isEmpty(self):
        '''判断线性表是否为空表'''
        pass

    @abstractmethod
    def length(self):
        '''返回线性表的长度'''
        pass

    @abstractmethod
    def get(self, i):
        '''读取并返回线性表中的第i个数据元素'''
        pass

    @abstractmethod
    def insert(self, i, x):
        '''插入x作为线性表中的第i个元素'''
        pass

    @abstractmethod
    def remove(self, i):
        '''删除线性表中的第i个元素'''
        pass

    @abstractmethod
    def indexOf(self, x):
        '''返回元素x首次出现的位序号'''
        pass

    @abstractmethod
    def display(self):
        '''输出线性表中各个元素的值'''
        pass


class Node(object):  # 构造函数初始化头节点
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkList(IList):
    def __init__(self):
        self.head = Node()

    def create(self, i, order):
        if order:
            self.create_tail(i)
        else:
            self.create_head(i)

    def create_tail(self, i):
        for item in i:
            self.insert(self.length(), item)

    def create_head(self, i):
        for item in i:
            self.insert(0, item)

    def clear(self):
        self.head.data = None
        self.head.next = None

    def isEmpty(self):
        return self.head.next == None

    def length(self):
        lengh = 0
        p = self.head.next
        while p is not None:
            p = p.next
            lengh += 1
        return lengh

    def get(self, i):
        p = self.head.next

        while i > 0 and p is not None:
            p = p.next
            i -= 1
        if i < 0 or p is None:
            raise Exception("第" + i + "个元素不存在")
        return p.data

    def insert(self, i, x):  # 把元素x插入位置i
        p = self.head
        j = -1
        while j < i - 1 and p is not None:
            p = p.next
            j += 1
        if j > i - 1 and p is None:
            raise Exception("插入位置错误")
        s = Node(x, p.next)
        p.next = s

    def remove(self, i):
        p = self.head
        j = -1# 指针停留在前驱节点的前提条件
        while j < i - 1 and p is not None:
            p = p.next  # 指针停留在前驱节点
            j += 1
        if j > i - 1 or p is None:
            raise Exception("删除位置不合法")
        p.next = p.next.next #前驱结点

    def indexOf(self, x):
        p = self.head.next
        j = 0
        while p is not None and not (p.data == x):
            p = p.next
            j += 1
        if p is not None:
            return j
        else:
            return -1

    def display(self):
        p = self.head.next
        while p is not None:
            print(p.data, end=" ")
            p = p.next
    def _reverse1(self):
        p=self.head.next
        self.head.next=None
        while p is not None:
                q=p.next
                p.next=self.head.next
                self.head.next=p
                p=q
    def _reverse2(self):
        
        prev=None
        while self.head :
            curr=self.head
            self.head=self.head.next
            curr.next=prev
            prev=curr
        

if __name__ == '__main__':
    data = [i for i in range(10)]
    ii = LinkList()
    ii.create(data, True)
    ii._reverse2()
    ii.display()



    # print()  # 换行
    # '''判断是否为空'''
    # if ii.isEmpty():
    #     print("空")
    # else:
    #     print("不为空");

    # '''在第三个位置插入元素8'''
    # print()  # 换行
    # ii.insert(3, 8)
    # ii.display()

    # '''元素4第一次出现的位置'''
    # print()
    # print(ii.indexOf(4))

    # '''删除第五个结点'''
    # print()
    # ii.remove(5)
    # ii.display()
