from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline().rstrip())
	for tc in range(N): 
		n = int(stdin.readline().rstrip())
		res = ''
		mu = 1
		cnt = 0 
		while n > 0:
			tmp = (n % 10) * mu
			if tmp != 0:
				res =str(tmp) + ' ' + res 
				cnt+=1
			n = n / 10
			mu *=10
		stdout.write(str(cnt)+'\n')
		stdout.write(str(res)+'\n')
if __name__ == "__main__": 
	main()