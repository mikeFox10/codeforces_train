'''


'''
from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline())
	for i in range(n):
		tc = int(stdin.readline())
		arr = [int(x) for x in stdin.readline().split()] 
		arr2 = [int(x) for x in stdin.readline().split()] 
		arr.sort()
		arr2.sort()
		r = ' '.join(map(str,arr))
		r2 = ' '.join(map(str,arr2))
		stdout.write(r+'\n')
		stdout.write(r2+'\n')
if __name__ == "__main__": 
	main()