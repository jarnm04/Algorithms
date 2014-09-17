#Joshua Rinaldi
#101902285
#9/17/14
#HW2

import math
import random
import time
import array

def isPrime(q):
	if (q == 1):
		q = 2
	p = False
	a = random.randint(1, 1000)
	if (a == 1):
		a = 2
	if (a**(q-1) % q == 1):
		p = True
	return p

def randPrime(n):
	f = 6
	while (not (isPrime(f)) or not (isPrime(f)) or not (isPrime(f)) or not (isPrime(f))):
		f = abs(random.getrandbits(n))
		if (f == 0):
			f = 6
	return f
	
def findE(t, n):
	e = randPrime(n)
	while (e >= t | t % e == 0):
		e = randPrime(n)
	return e
	
def encode(x, e, N):
	return ((x ** e) % N)
	
def decode(y, d, N):
	return ((y**d) % N)

def main():
	#A = array.array('i')
	#A.append(5)
	#A.append(6)
	#A.append(7)
	x = 3104
	d = 0
	for i in range (8, 11):
		timeA1 = time.time()
		p = randPrime(i)
		q = randPrime(i)
		N = p*q
		t = (p-1)*(q-1)
		e = findE(t, i)
		timeA2 = time.time()
		timeA = timeA2 - timeA1
		d = 0
		for i in range (0, t):
			if ((e * i) % t == 1):
				d = i
		print(p, q, N, e, d, x)
		timeB1 = time.time()
		y = encode(x, e, N)
		timeB2 = time.time()
		timeB = timeB2 - timeB1
		print (y)
		timeC1 = time.time()
		z = decode(y, d, N)
		timeC2 = time.time()
		timeC = timeC2 - timeC1
		print (z)
		print (timeA)
		print (timeB)
		print (timeC)
		
if __name__ == "__main__":
    main()
