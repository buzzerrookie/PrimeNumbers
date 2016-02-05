import sys
import math

# This script only gives positive entries in a triple.
# You can generate negative entries on your own.
# n = 2x^2 + y^2 + 8z^2
def xyz(n):
	print("X Y Z")
	x = 0
	while 2 * x ** 2 <= n:
		y = 0
		while (2 * x ** 2 + y ** 2) <= n:
			temp = math.sqrt((n - (2 * x ** 2 + y ** 2)) / 8)
			z = math.floor(temp)
			if temp == z:
				print(x, y, z)
			y += 1
		x += 1
	print("-------------")

# n = 2a^2 + b^2 + 32c^2
def abc(n):
	print("A B C")
	a = 0
	while 2 * a ** 2 <= n:
		b = 0
		while (2 * a ** 2 + b ** 2) <= n:
			temp = math.sqrt((n - (2 * a ** 2 + b ** 2)) / 32)
			c = math.floor(temp)
			if temp == c:
				print(a, b, c)
			b += 1
		a += 1

if __name__ == '__main__':
	# command line option
	if len(sys.argv) != 2:
		print("Usage: ./tunnell.py <n>")
		sys.exit(-1)
	try:
		n = int(sys.argv[1])
	except:
		print("Please input area in interger!")
		sys.exit(-2)
	xyz(n)
	abc(n)
