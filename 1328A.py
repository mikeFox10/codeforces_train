from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline()) 
	for x in range(n):
		a, b = [int(x) for x in stdin.readline().split()] 
		if a == (a / b) * b:
			stdout.write(str(0)+'\n')
			continue
		temp = ((a / b) + 1) * b 
		res = abs(a - temp)
		stdout.write(str(res)+'\n')

		 
if __name__ == "__main__": 
	main()