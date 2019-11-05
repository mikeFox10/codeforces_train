from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline())
	arr = [int(x) for x in stdin.readline().split()] 
	cache = {}
	for x in arr: 
		if x not in cache:
			cache[x] = True
	for x in range(1,3002):
		if x not in cache:
			stdout.write(str(x)+'\n')
			break
if __name__ == "__main__": 
	main()