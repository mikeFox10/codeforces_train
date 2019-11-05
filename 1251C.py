from sys import stdin, stdout  

def solve(minimize):
	odd = []
	even = []
	res = ''
	for i in minimize:
		num = int(i)
		if num & 1:
			odd.append(num)
		else:
			even.append(num)
	indexO = 0
	indexE = 0
	print(even)
	print(odd)
	for z in range(len(odd) + len(even) -1 ):
		if indexO == len(odd):
			res +=  "".join(str(x) for x in even[indexE:])
			break
		if indexE == len(even):
			res +=  "".join(str(x) for x in odd[indexO:])
			break
		if even[indexE] < odd[indexO]:
			res+=str(even[indexE])
			indexE+=1
		else:
			res+=str(odd[indexO])
			indexO+=1
	return res



def main(): 
	n = stdin.readline() 

	res = ''
	for x in range(int(n)): 
		minimize = stdin.readline().rstrip()
		res += solve(minimize) + '\n'
	stdout.write(res)
if __name__ == "__main__": 
	main()