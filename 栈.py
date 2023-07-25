
# //image.png顺序栈
# class SqStack():
        
#     def __init__ (self,maxsize):
#         self.maxsize=maxsize
#         self.stackElem=[None]*self.maxsize
#         self.num=0 
        
#     def isEmpty(self):
#         return self.num==0
        
#     def clear(self):
#         self.num=0
        
#     def length(self):
#         return self.num
        
#     def peek(self):
#         if not self.isEmpty :
#             return self.stackElem[self.num-1]#存进第一个元素的时候，下标是0，top=1
        
#     def push(self,x):
#         if self.num==self.maxsize:
#             raise Exception("full");
#         else:
#             self.stackElem[self.num-1]=x
#         self.num+=1
        
#     def pop(self):
#             if self.isEmpty():
#                 raise Exception("NO ELEMENTS CAN POP");
#             else:
#                 self.num-=1
#                 return self.stackElem[self.num]
        
# 
    
#一般列表就可以实现栈，用append和pop方法
class Stack():
    def __init__(self) -> None:
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()
    def get_top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None
    def isEmpty(self):
        return  len(self.stack)==0
    
# if __name__=='__main__':
#     a=Stack()
#     a=[i for i in range(10)]
#     print(a)
#     print(a.pop())





def IsMatched(s):
    left={'{',"[","("}
    stack=Stack()
    for ch  in s:
        if ch in left:
            stack.push(ch)
        else:
            if stack.isEmpty():
                return False
            elif stack.get_top() in left:
                stack.pop()
            else:
                return False
    if stack.isEmpty():
        return True
    else:
        return False
    
    
#测试函数
stringa = "(){}[({})]{"
print(IsMatched(stringa))   