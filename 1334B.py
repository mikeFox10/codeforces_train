from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline()) 
	for i in range(N):
		n , x = [int(x) for x in stdin.readline().split()]
		arr = [int(x) for x in stdin.readline().split()]
		res = 0
		arr = sorted(arr,reverse=True)
		#sarr = arr.sort(reverse=True)
		summ = []
		for idx in range(len(arr)):
			if idx == 0:
				summ.append(arr[idx])
				continue
			summ.append(arr[idx] + summ[idx - 1])
		ind = -1 
		print(arr)
		print(summ)
		for elesum in summ:
			ind +=1 
			if elesum / float(ind + 1) >= x:
				res = ind + 1
			else:
				break
		stdout.write(str(res)+'\n')
if __name__ == "__main__": 
	main()