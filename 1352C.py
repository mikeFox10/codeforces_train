from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N): 
		n, k = [int(x) for x in stdin.readline().split()] 
		toAdd = (k - 1) / (n - 1)
		stdout.write(str( k + toAdd)+'\n')
if __name__ == "__main__": 
	main()