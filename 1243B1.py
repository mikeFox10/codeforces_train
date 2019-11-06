from sys import stdin, stdout  
  
def main(): 
	k = int(stdin.readline() )
	while k > 0:
		k-=1
		n = int(stdin.readline())
		s = stdin.readline()
		t = stdin.readline()
		ar = []
		ar2 = []
		for index, car in enumerate(s):
			if car != t[index]:
				ar.append(car)
				ar2.append(t[index])
			if len(ar) > 2:
				break
		#print(ar)
		if len(ar) == 2 and len(ar2) == 2:
			if ar[0] == ar[1] and ar2[0] == ar2[1] :
				stdout.write('Yes' + '\n')
			else:
				stdout.write('No' + '\n')
		else:
				stdout.write('No' + '\n')
if __name__ == "__main__": 
	main()