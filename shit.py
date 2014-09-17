import random
import math
import time 
import array

def selectionSort(A, n):
    for i in range(0, n-2):
    	i_min = i
	for j in range(i+1, n-1):
	    if A[j] < A[i_min]:
	       i_min = j
        temp = A[i]
    	A[i] = A[i_min]
    	A[i_min] = temp

def main():
    for i in range (3, 7):
        T = array.array('f')
    	end = 10**i
	for n in range (0, 10):
	    A = array.array('i')
	    for z in range (0, end):
	    	A.append(random.randint(0, 1000000))
	    time1 = time.time()
	    selectionSort(A, len(A))
	    time2 = time.time()
            timeTot = time2-time1
	    print (timeTot)
            T.append(timeTot)
        g = 0
	for x in range (0, len(T)):
            g = g + T[x]
        print(g/len(T))
        print()

if __name__ == "__main__":
    main()
