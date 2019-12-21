from sys import stdin, stdout  
  
def isPrime(n) : 
	# Corner cases 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True
	if (n % 2 == 0 or n % 3 == 0) : 
		return False
  
	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6
  
	return True

def main(): 
	n = int(stdin.readline())
	
	if n == 1:
		stdout.write('9 8\n')
	else:
		solved = False
		b = 4
		a = None
		#if b % 2 != 0:
		#	b=b+1
		while solved == False:
			if b+n % 2 == 0 or not isPrime(b+n):
				a = b+n
				solved = True
			else:
				b = b+2
		stdout.write('{} {}'.format(a,b)+'\n')
if __name__ == "__main__": 
	main()