from sys import stdin, stdout  
  
def main(): 
	k = int(stdin.readline() )
	while k > 0:
		k-=1
		n = int(stdin.readline())
		arr = [int(x) for x in stdin.readline().split()] 
		arr.sort()
		#print(arr)
		lastIndex = -1
		if arr[0] == arr[len(arr)-1]:
			stdout.write(str(arr[0])+'\n')
			continue
			
		for i in range(n):
			if arr[i] <= len(arr)-i:
				lastIndex = i
			else:
				lastIndex = max(arr[lastIndex], len(arr) - i)
				break
		stdout.write(str(lastIndex)+'\n')
if __name__ == "__main__":
	main()
'''

1 1 5 5 5

1 3 4 4 5

'''