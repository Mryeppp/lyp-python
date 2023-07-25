class Queue:
    def __init__(self) -> None:
        self.queue=[]
    def isempty(self):
        return self.queue==[]
    def enqueue(self,queue):
        self.queue.insert(0,queue)
    def dequeue(self):
        p=self.queue[-1]
        self.queue.pop()
        print(p)
    def length(self):
        return len(self.queue)
    def dispaly(self):
        for i in range(self.length()):
            print(self.queue[i],end=" ")
if __name__=="__main__":
    q=Queue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.dispaly()
    print()
    q.dequeue()
    q.dispaly()