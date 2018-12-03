def table(n):
	for i in range(1,11):
		print(""+str(n)+"*"+str(i)+"="+str(n*i))
if __name__ == '__main__':
	print("Enter Number:")
	n = int(input())
	print("Table of "+str(n)+":")
	table(n)
