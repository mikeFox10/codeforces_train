from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline()) 
	sol = 0
	for i in range(1,n+1):
		sol+=(1.0/i)
	stdout.write(format(sol, '.12f')+'\n')
if __name__ == "__main__": 
	main()