class Queue:
	def __init__(self,size=100):
		self.front=0
		self.rare=0
		self.queue=[0 for _ in range(size)]
	
	def push(self,element):
		self.rare=(self.rare+1)%self.size
		self.queue[self.rare]=element
	
	def pop(self):
		self.front=(self.front+1)%self.size
		return self.queue[self.front]
	
	def isEmpty(self):
		return self.rare == self.front
	
	def isFilled(self):
		return (self.rare+1)%self.size==self.front


  