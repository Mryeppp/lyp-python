#cmd 编译py文件的方法： python 文件名.py
from abc import ABCMeta,abstractmethod,abstractproperty
class IList(metaclass = ABCMeta):
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
        
        
class SqList(IList):
    def __init__(self, maxSize):
        self.curLen = 0 # 顺序表的当前长度
        self.maxSize = maxSize # 顺序表的最大长度
        self.listItem = [None] * self.maxSize # 顺序表存储空间

    def clear(self):
        '''将线性表置成空表'''
        self.curLen = 0

    def isEmpty(self):
        '''判断线性表是否为空表'''
        return self.curLen == 0

    def length(self):
        '''返回线性表的长度'''
        return self.curLen

    def get(self, i):
        '''读取并返回线性表中的第i个数据元素'''
        if i < 0 or i > self.curLen - 1:
            raise Exception("第"+i+"个元素不存在") 
        return self.listItem[i]

    def insert(self, i, x):
        '''插入x作为线性表中的第i个元素'''
        if self.curLen == self.maxSize:
            raise Exception("顺序表满")
        if i < 0 or i > self.curLen:
            raise Exception("插入位置非法")
        for j in range(self.curLen, i-1, -1):
            self.listItem[j] = self.listItem[j-1]
        self.listItem[i] = x
        self.curLen += 1

    def remove(self, i):
        '''删除线性表中的第i个元素'''
        if i < 0 or i > self.curLen - 1:
            raise Exception("删除位置非法")
        for j in range(i, self.curLen):
            self.listItem[j] = self.listItem[j+1]
        self.curLen -= 1

    def indexOf(self, x):
        '''返回元素x首次出现的位序号'''
        for i in range(self.curLen):
            if self.listItem[i] == x:
                return i
        return -1

    def display(self):
        '''输出线性表中各个元素的值'''
        for i in range(self.curLen):
            print(self.listItem[i], end=' ')

# q=SqList(5) 
# for i,x in zip(range(5),[89,93,92,90,100]):
     # #zip()函数内存放的是一个或者多个迭代器，可以同时进行遍历
    # q.insert(i,x)
# res=q.indexOf(90)
# if res==-1:
    # print("不存在90分")
# else:
    # print("位置为%s"%res)
    
    
    
    
# L=SqList(26)
# for i in range(26):
    # L.insert(i,chr(ord('a')+i))
# while True：
    # i=int(input("输入需要查询元素的序号:\n"))
    # if i>0 and i <25:
        # print("第%s个元素的直接前驱为%s"%(i+1,L.get(i-1)))
        # print("第%s个元素的直接后驱为%s"%(i+1,L.get(i+1)))
    # elif i==0:
        # print("第%s个元素的直接前驱不存在"%(i+1,))
        # print("第%s个元素的直接后驱为%s"%(i+1,L.get(i+1)))
    # elif i==25: 
        # print("第%s个元素的直接前驱为%s"%(i+1,L.get(i-1)))
        # print("第%s个元素的直接后驱不存在"%(i+1,))
    # else:
    # print("位置非法")
   


# L= [1, 2, 1, 3, 1 ]
# def Deletex1(L,x):
    # k=0
    # x=1
    # for j in range(L.getsize()):
        # if L[j]!=x:
            # L[k]=L[j]
            # k+=1
    # L.size=k
# print(L)


SL=SqList(15)

'''创建顺序表，将元素 2，5，16，55，8 依次存入 SL 中。判断 SL 是否为空。'''
for i,x in zip(range(5),[2,5,16,55,8]):
    SL.insert(i,x)
if(SL.isEmpty()==False):
    print("线性表不为空")
elif(SL.isEmpty==True):
    print("线性表为空")

'''增加顺序表元素6，7，8，9'''
for j,h in zip(range(SL.length(),SL.length()+5),[6,7,8,9]):
    SL.insert(j,h)

'''查找序号为2的元素'''
SL.get(2)

'''在序号为2的位置插入元素8'''
SL.insert(2,8)

'''输出 SL 中元素的个数。'''
print("线性表的长度为：%d"%SL.length())

'''删除值为 16 的元素'''
SL.remove(SL.indexOf(16))

'''将 SL 中元素依次输出。''' 
SL.display()
