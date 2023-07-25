class CirSeqQueue:
    def __init__(self, init_len=8):
        self.MaxQueueSize=init_len
        self.s=[None for x in range(0,self.MaxQueueSize)]
        self.front=0
        self.rear=0
 
    def IsEmptyQueue(self):
        if self.front==self.rear:
            iQueue=True
        else:
            iQueue=False
        return iQueue
 
    def EnQueue(self,x):
        if(self.rear+1)%self.MaxQueueSize!=self.front:
            self.rear=(self.rear+1)%self.MaxQueueSize
            self.s[self.rear]=x
        else:
            print("队列已满")
            return
 
    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空")
            return
        else:
            self.front=(self.front+1)%self.MaxQueueSize
            return self.s[self.front]
 
def yanghui(n):
    q = CirSeqQueue(1000)
    for i in range(0,n):
        print(' ',end='')
    #输出第一行的1
    print(1)
    #从第二行开始处理
    q.EnQueue(0)
    q.EnQueue(1)
    q.EnQueue(1)
    k=0
 
    while k<n:
        #每行前面的空格数目逐渐减1
        for i in range(1,n-k):
            print(' ',end='')
        #将一个0入队，来标志一行的结尾
        q.EnQueue(0)
        temp=q.DeQueue()
        value=q.DeQueue()
        q.EnQueue(0)
 
        while value!=0:
            print(value,end=" ")
            q.EnQueue(value+temp)
            temp=value
            value=q.DeQueue()
 
        q.EnQueue(value + temp)
        print("\n",end="")
        k=k+1
 
if __name__ == '__main__':
    q = CirSeqQueue(1000)
    yanghui(10)