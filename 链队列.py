class Node():
  #
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

class linkqueue():
  #
  def __init__(self):
    self.front=None
    self.rear=None
 
  def clear(self):
    self.front=None
    self.rear=None
  
  #self.rear==self.front!! 错误
  def isEmpty(self):
   return  self.front is None
 
 #
  def length(self):
    i=0
    p = self.front
    while p is not None:
      p=p.next
      i+=1
    return i
  
  def peek(self):
    if self.isEmpty():
      return  None
    else:
      return self.front.data
  
  def pop(self):
    if self.isEmpty():
      return None
    else: 
      p=self.front
      self.front=self.front.next
      #
      if p==self.rear:
        self.rear=None
    return p.data
  
  def push(self,ele):#插入队尾
    s=Node(ele,None)
    if not self.isEmpty():
      self.rear.next=s
    else:
      self.front=s 
    self.rear=s
      
 
  def display(self):
    p=self.front
    while p is not None:
        print(p.data,end=" ")
        p=p.next

    
if __name__== "__main__":
    linkq=linkqueue()
    print(linkq.isEmpty())
    
   
    for i in range(10) :
      linkq.push(i)

    linkq.display()

    linkq.pop()
    print("")
    linkq.display()

    print("")
    print(linkq.peek())