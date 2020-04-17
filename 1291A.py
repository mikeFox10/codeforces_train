from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline())
	for x in range(n):
		tc = int(stdin.readline())
		s = (stdin.readline())
		res = ''
		end = False
		suma = 0
		finded = False
		for i in range(tc-1, 0, -1):
			ints = int(s[i])
			if not end and  ints % 2 != 0:
				res = s[i] 
				suma = ints
				end = True
				continue
			if end:
				res = s[i] + res
				suma+=ints
				if s[i] != '0' and suma % 2 == 0:
					finded = True
					break
		if not finded and end:
			if int(s[0]) % 2 != 0:
				res =  s[0] + res
				finded = True
		if finded:
			stdout.write(res+'\n')
		else:
			stdout.write('-1\n')

if __name__ == "__main__": 
	main()