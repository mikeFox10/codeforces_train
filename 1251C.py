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

	while(indexE != len(even) and indexO != len(odd)):
		if even[indexE] <odd[indexO]:
			res+=str(even[indexE])
			indexE+=1
		else:
			res+=str(odd[indexO])
			indexO+=1
	#print(even)
	#print(odd)
	#print(res, indexE, indexO)
	if indexE == len(even):
		# res+=''.join(str(e) for e in even[indexE:])
		res+=''.join(str(e) for e in odd[indexO:])

	elif indexO == len(odd):
		res+=''.join(str(e) for e in even[indexE:])
		# res+=''.join(str(e) for e in odd[indexO:])

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
