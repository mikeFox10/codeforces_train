from sys import stdin, stdout  
import math
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N):
		n, m , k = [int(x) for x in stdin.readline().split()]
		hand = int(n / k)
		if m == 0:
			stdout.write(str(0)+'\n')
			continue
		if m <= hand:
			stdout.write(str(m)+'\n')
			continue
		lef = m - hand
		ans = math.ceil(float(lef) / (k - 1))
		# print(ans , lef, k-1, float(lef) / k )
		stdout.write(str(int (hand - ans))+'\n')
if __name__ == "__main__": 
	main()