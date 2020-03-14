from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline())
	for i in range(N):
		n = int(stdin.readline())
		arr = [int(x) for x in stdin.readline().split()] 
		sorted(arr)
		dd = {}
		for x in arr: 
			if x not in dd:
				dd[x] = True
		stdout.write(str(len(dd))+'\n')
if __name__ == "__main__": 
	main()