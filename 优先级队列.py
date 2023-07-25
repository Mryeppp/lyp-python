class PriorityNode:
    def __init__(self,data=None,next=None,priority=None):
        self.data=data
        self.next=next
        self.priority=priority
class PriorityQueue:
    def __init__(self):
        self.front=None;
        self.rear=None;
    def clear(self):
        self.front=None
        self.rear=None
    def isEmpty(self):
        return self.front is None
    def length(self):
        if not self.isEmpty():
            size=0
            p=self.front
            while(p is not None):
                p=p.next
                size+=1
            return size
    def peek(self):
        p=self.front
        if not self.isEmpty():
            return p.data
        else:
            return None
    def offer(self,x,priority):
        s=PriorityNode(x,None,priority)
        if not self.isEmpty():
            p=self.front
            q=self.front
            while p is not None and p.priority>=s.priority:
                q=p
                p=p.next                                       
                #前后指针
                
                #三情况：p是队尾，p是队首，p是队中
            if  p is None:
                self.rear.next = s
                self.rear = s
            elif p == self.front:
                s.next = self.front
                self.front =s 
            else:
                s.next = p
                q.next = s                         
        else:
            self.front = self.rear = s
    
    
    
    def poll(self):
        if self.isEmpty():
           return None
        p=self.front
        self.front=self.front.next
        if p == self.rear:
            self.rear=None
        return p.data
    
    
    
    def display(self):
        p=self.front
        while p is not None:
            print(p.data,end=" ")
            p=p.next
'''
可以模拟操作系统的进程管理问题，要求优先级高的进程
先获取cpu,假设操作系统中的进程由进程号和优先级构成
进程号1234，优先级1，2，3，4，约定数值越大优先级越高

'''
cpu=PriorityQueue()
cpu.offer(4,50)
cpu.offer(3,10)
cpu.offer(2,30)
cpu.offer(1,20)
print(cpu.display()) #3124
print("进程服务的顺序为：")



print(cpu.poll(),end=" ")