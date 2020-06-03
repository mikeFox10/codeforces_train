from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N): 
		n, k = [int(x) for x in stdin.readline().split()] 
		a = [int(x) for x in stdin.readline().split()] 
		b = [int(x) for x in stdin.readline().split()]
		
		a.sort()
		ans = []
		b.sort(reverse=True)
		for i in range(k):
			ans.append(max(a[i], b[i]))
		for i in range(k, n):
			ans.append(a[i])
		# print(a, b, ans, sum(ans))
		stdout.write(str(sum(ans))+'\n')
if __name__ == "__main__": 
	main()