from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N): 
		n, m = [int(x) for x in stdin.readline().split()] 
		stdout.write(str(min(2, n - 1) * m )+'\n')
if __name__ == "__main__": 
	main()