from sys import stdin, stdout  
  
def main(): 
	tc = int(stdin.readline()) 
	for tt in range(tc): 
		n, xx = [int(x) for x in stdin.readline().rstrip().split()] 
		arr = [int(x) for x in stdin.readline().rstrip().split()]
		res = 0 
		dd = {}
		count = 1
		while xx > 0:
			if count not in arr:
				xx-=1
			if xx> 0: 
				count+=1
		if count+1 in arr:
			count+=1
		stdout.write(str(count)+'\n')
if __name__ == "__main__": 
	main()