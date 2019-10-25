from sys import stdin, stdout  
'''
DIVIDE AND CONQUER , STRINGS
'''

def getMiniumStringSorted(stringEval):
	if len(stringEval) % 2 == 1:
		return stringEval
	s1 = getMiniumStringSorted(stringEval[0:len(stringEval)/2])
	s2 = getMiniumStringSorted(stringEval[len(stringEval)/2: len(stringEval)])
	if s1 < s2:
		return s1+s2
	return s2+s1




def main(): 
	A = stdin.readline().rstrip() 
	B = stdin.readline().rstrip() 
	
	response = ''
	if A == B: 
		response = 'YES'
	if len(A) % 2 == 0 and len(B) % 2 == 0 and response != 'YES':
		a1 = A[:len(A)/2]
		a2 = A[len(A)/2:]

		b1 = B[:len(B)/2]
		b2 = B[len(B)/2:]

		if a1 == b1 and a2 == b2:
			response == 'YES'
		
		if a1 == b2 and a2 == b1:
			response == 'YES'

		if response != 'YES':
			a1 = getMiniumStringSorted(a1)
			a2 = getMiniumStringSorted(a2)
			b1 = getMiniumStringSorted(b1)
			b2 = getMiniumStringSorted(b2)
			#print(a1, a2, b1,b2, 'DE')
			if a1 == b1 and a2 == b2:
				response = 'YES'
			if a1 == b2 and a2 == b1:
				response = 'YES'
	#print(response, 'res')
	if response != 'YES':
			response = 'NO'
	stdout.write(response+'\n')
if __name__ == "__main__": 
	main()