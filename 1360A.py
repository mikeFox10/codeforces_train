from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N): 
		a, b = [int(x) for x in stdin.readline().split()] 
		maxx = max(a,b)
		doubl = min(a,b) * 2
		ans = max(maxx, doubl) * max(maxx, doubl)
		stdout.write(str(ans)+'\n')
if __name__ == "__main__": 
	main()