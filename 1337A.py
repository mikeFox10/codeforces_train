from sys import stdin, stdout  
  
def main(): 
	N = int(stdin.readline()) 
	for x in range(N): 
		a, b,c, d = [x for x in stdin.readline().split()] 
		stdout.write(b+ ' ' + c+ ' ' + c +'\n')
if __name__ == "__main__": 
	main()