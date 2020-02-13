'''


'''
from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline() )
	for x in range(n): 
		a = stdin.readline()
		b = stdin.readline()
		c = stdin.readline()
		sww = 0
		res = 'YES'
		for chaidx in range(len(c)):
			if a[chaidx] == c[chaidx] or c[chaidx] == b[chaidx]:
				res = 'YES'
			else:
				res = 'NO'
				break
		stdout.write(str(res)+'\n')
if __name__ == "__main__": 
	main()