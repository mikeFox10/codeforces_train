from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline())
	while n > 0:
		n-=1
		r,g,b = [int(x) for x in stdin.readline().split()] 
		res = 0
		ord = [r,g,b]
		ord.sort()
		# print(ord)
		if ord[2] < ord[0] + ord[1] :
		
			rest = ord[2] - ord[1]
			res = ord[2]
			ord[0] = ord[0] - rest
			res+=(ord[0]//2)
			stdout.write(str(res)+"\n")

		else:
			res = min(ord[2], ord[0] + ord[1])
			#print("resss", res)
			stdout.write(str(res)+"\n")
if __name__ == "__main__": 
	main()


