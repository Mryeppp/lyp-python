class SqQueue():
    def __init__(self,maxsize) -> None:
        self.maxsize=maxsize 
        self.queueElem=[None]*self.maxsize
        self.rare=0;#队尾的下一个位置
        self.front=0;#队首的位置
    def clear(self):
        self.front=0
        self.rare=0
    def isEmpty(self):
        return self.front==self.rare
    def length(self):
        return self.rare-self.front
    def peek(self):#返回队首元素
        if self.isEmpty():
            return  None
        else:
            return self.queueElem[self.front] 
    def offer(self,x):
        #插入队尾
        if self.rare==self.maxsize:
            raise Exception("full")
        else:
            
            self.queueElem[self.rare]=x;
            self.rare+=1
            
    def poll(self):
        #删除队首元素并返回
        if self.isEmpty():
            raise Exception("no elements")
        else:
            head=self.queueElem[self.front]
            del self.queueElem[self.front] #!!!
            self.front+=1
            return head
    def display(self):
        for i in range(self.rare-self.front):
            print(self.queueElem[i],end=" ")


if __name__ == "__main__":
    s=SqQueue(50)
    s.offer(100)
    s.offer(45)
    s.offer(37)
    s.offer(955)
    s.offer(78)
    print(s.length())
    s.display()
    print()
    print(s.peek())
    print()
    print(s.poll())
    print()
    s.display()
    