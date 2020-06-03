from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N): 
		n = int(stdin.readline().rstrip())
		arr = [int(x) for x in stdin.readline().split()] 
		arr.sort()
		last = float('inf')
		ans = None
		for i in range(1, len(arr)):
			if abs(arr[i] - arr[i - 1]) < last:
				last = abs(arr[i] - arr[i - 1])
		stdout.write(str(last)+'\n')
if __name__ == "__main__": 
	main()