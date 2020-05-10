from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N): 
		n0, n1, n2 = [int(x) for x in stdin.readline().split()] 
		ans = ''
		if n2 > 0:
			ans += '1' * (n2+1)
		if n1 > 0 and n2 == 0:
			ans += '1'
		if n1 > 0:
			zero = True
			while n1 > 0:
				if zero:
					ans += '0'
					zero = False
				else:
					ans += '1'
					zero = True
				n1-=1
		if len(ans) == 0:
			ans += '0'
		if n0 > 0:
			if ans[len(ans) - 1] == '0':
				ans = ans + ('0' * (n0))
			else:
				i = ans.find('0')
				ans = ans[:i] + '0' * (n0) + ans[i:]
		stdout.write(str(ans)+'\n')
if __name__ == "__main__": 
	main()