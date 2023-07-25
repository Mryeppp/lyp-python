def move(s,t):
	print(s,"->",t)
def hanoi(n,a,b,c):
	if n==1 :
		move(a,c)
	else:
		hanoi(n-1,a,c,b)
		move(a,c)
		hanoi(n-1,b,a,c)



hanoi(5,"a","b","c")