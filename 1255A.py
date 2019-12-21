from sys import stdin, stdout  
  
def main(): 
	ctr = [5,2,1]
	ctrM = [1,2,5]
	T = int(stdin.readline())
	while T>0:
		T-=1
		a, b = [int(x) for x in stdin.readline().split()] 
		arr = 1
		if a==b:
			print(0)
			continue
		dist = 0
		if a>b:
			dist = a - b
		else:
			dist = b - a
		res = dist // 5 + (dist % 5 ) // 2 + ((dist % 5 )%2 ) // 1
		print(res)

if __name__ == "__main__": 
	main()