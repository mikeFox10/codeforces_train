from sys import stdin, stdout  
  
def main(): 
	n = int(stdin.readline())
	for i in range(n):
		a, b, c, d = [int(x) for x in stdin.readline().split()] 
		x, y, x1, y1, x2, y2 = [int(x) for x in stdin.readline().split()] 
		res = 'YES'
		x = x  -  a  +  b
		y = y  - c + d
		if x < x1 or x > x2 or y < y1 or y > y2:
			res = 'NO'
		if x2 - x1 == 0 and (a > 0 or b > 0):
			res = 'NO'
		if y2 - y1 == 0 and (c > 0 or d > 0):
			res = 'NO'

		stdout.write(res+'\n')
if __name__ == "__main__": 
	main()