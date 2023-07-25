def resursion(n):
	if n < 0 :
		return None
	elif n == 0 :
		return 0
	elif n == 1 :
		return 1
	else:
		return resursion(n-1)+resursion(n-2)


if __name__ == "__main__":
	print(resursion(10))
	print("hello github")