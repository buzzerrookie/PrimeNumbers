import sys

def primes(n):
	isprime = [True] * (n + 1)
	isprime[0] = False
	isprime[1] = False
	for i in range(2, n + 1):
		if not isprime[i]:
			continue
		isprime[i] = True
		print(i)
		j = 2
		while (j * i) <= n:
			if isprime[j * i]:
				isprime[j * i] = False
			j += 1

if __name__ == '__main__':
	# command line option
	if len(sys.argv) != 2:
		print("Usage: ./primes.py <n>")
		sys.exit(-1)
	try:
		n = int(sys.argv[1])
	except:
		print("Please input a interger!")
		sys.exit(-2)
	primes(n)
