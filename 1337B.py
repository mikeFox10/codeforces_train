from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline()) 
  
	for x in range(N): 
		x, n, m = [int(x) for x in stdin.readline().split()] 
		while n > 0 and x/2 + 10 < x:
			x = x/2 + 10
			n-=1 
		if x <= m*10:
			stdout.write(str('YES')+'\n')
		else:
			stdout.write(str('NO')+'\n')

if __name__ == "__main__": 
	main()