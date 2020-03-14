from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline()) 
	for tc in range(n):
		a, b  = [int(x) for x in stdin.readline().split()] 
		res = 0
		difference = a - b
		if difference > 0 and difference % 2 == 0:
			res = 1
		elif difference < 0 and difference % 2 == 0:
			res = 2
		elif difference > 0 and difference % 2 != 0:
			res = 2
		elif difference < 0 and difference % 2 != 0:
			res = 1
		stdout.write(str(res)+'\n')
if __name__ == "__main__": 
	main()