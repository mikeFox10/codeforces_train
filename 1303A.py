'''


'''
from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline()) 
	for x in range(n): 
		n = stdin.readline()
		res = 0

		if '1' not in n:
			stdout.write('0\n')
			continue
		ini = n.index('1')
		fin = len(n) - n[::-1].index('1') - 1
		for cha in range(ini, fin):
			if n[cha] == '0':
				res+=1
		stdout.write(str(res)+'\n')
if __name__ == "__main__": 
	main()