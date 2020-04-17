from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline()) 
	for x in range(n):
		l = stdin.readline()
		a = stdin.readline().rstrip()
		resa = '1'
		resb = '1'
		sw = None
		for i in range(1, len(a)):
			if sw == 1:
				resa+='0'
				resb+=a[i]
				continue
			
			if sw == None and a[i] == '1':
				sw = 1
				resa+='1'
				resb+='0'
				continue
			if a[i] == '2':
				resa+='1'
				resb+='1'
				continue
			if a[i] == '0':
				resa+='0'
				resb+='0'
				continue
		stdout.write(str(resa)+'\n')
		stdout.write(str(resb)+'\n')

		 
if __name__ == "__main__": 
	main()