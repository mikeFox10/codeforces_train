from sys import stdin, stdout  
import math
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N): 
		a, b, c, d = [int(x) for x in stdin.readline().split()] 
		if  (c <= d and b < a):
			stdout.write(str(-1)+'\n')
			continue
		if a <= b:
			stdout.write(str(b)+'\n')
			continue
		obj = a - b 
		nTimes = int(math.ceil(obj / (c - float(d))))
		ans = nTimes * c + b
		stdout.write(str(ans)+'\n')
if __name__ == "__main__": 
	main()