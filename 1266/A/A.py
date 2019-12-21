from sys import stdin, stdout  
def main(): 
	n = stdin.readline() 
	for x in range(int(n)): 
		tc = stdin.readline().rstrip()
		swZero = None
		if tc.find('0') == -1:
			print('cyan')
			continue
		sum  = 0
		even = 0
		for i in tc:
			ii = int(i)
			sum+=ii
			if ii % 2 == 0:
				even+=1
		if sum % 3 == 0 and even > 1:
			stdout.write('red\n')
		else:
			stdout.write('cyan\n')

if __name__ == "__main__": 
	main()