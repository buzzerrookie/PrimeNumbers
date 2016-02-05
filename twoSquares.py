import sys
import math

def twoSquares(n):
	a = 1
	while (2 * a ** 2) <= n:
		temp = math.sqrt(n - a ** 2)
		b = math.floor(temp)
		if b == temp:
			print(a, b)
		a += 1

if __name__ == '__main__':
	# command line option
	if len(sys.argv) != 2:
		print("Usage: ./twoSquares.py <n>")
		sys.exit(-1)
	try:
		n = int(sys.argv[1])
	except:
		print("Please input a interger!")
		sys.exit(-2)
	twoSquares(n)
