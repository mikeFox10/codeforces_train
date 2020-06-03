from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N): 
		n = int(stdin.readline().rstrip())
		ans = 0
		cntRing = 8 
		for i in range(1, n/2 + 1):
			ans = ans + i * cntRing
			cntRing+=8
		stdout.write(str(ans)+'\n')
if __name__ == "__main__": 
	main()