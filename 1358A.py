from sys import stdin, stdout  
import math
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N): 
		n, m  = [int(x) for x in stdin.readline().split()] 
		ans = math.ceil((n*m)/2.0)
		stdout.write(str(int(ans))+'\n')
if __name__ == "__main__": 
	main()