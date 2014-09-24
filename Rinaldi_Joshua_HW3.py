#Joshua Rinaldi
#101902285
#9/24/14
#HW3

import math
import array

def FindMaxCrossingSubarray(A, low, mid, high):
	leftSum = -1000000000000
	sum = 0
	maxLeft = mid
	maxRight = mid
	for i in range (mid, low, -1):
		sum = sum + A[i]
		if(sum > leftSum):
			leftSum = sum
			maxLeft = i
	rightSum = -1000000000000
	sum = 0
	for j in range (mid + 1, high, 1):
		sum = sum + A[j]
		if (sum > rightSum):
			rightSum = sum
			maxRight = j
	return(maxLeft, maxRight, leftSum + rightSum)

def FindMaximumSubarray(A, low, high):
	if (high == low):
		return (low, high, A[low])
	else:
		mid = int(math.floor((low + high)/2))
		(leftLow, leftHigh, leftSum) = FindMaximumSubarray(A, low, mid)
		(rightLow, rightHigh, rightSum) = FindMaximumSubarray(A, mid+1, high)
		(crossLow, crossHigh, crossSum) = FindMaxCrossingSubarray(A, low, mid, high)
		if (leftSum >= rightSum and leftSum >= crossSum):
			return (leftLow, leftHigh, leftSum)
		elif (rightSum >= leftSum and rightSum >= crossSum):
			return (rightLow, rightHigh, rightSum)
		else:
			return (crossLow, crossHigh, crossSum)
			
def differenceArray(A):
	B = array.array('f')
	for i in range(1, len(A)):
		B.append(A[i]-A[i-1])
	return B

def main():
	F = open('apple.txt', 'r')
	A = array.array('f')
	for line in F:
		A.insert (0, float(line))
	B = differenceArray(A)
	(low, high, sum) = FindMaximumSubarray(B, 0, len(B)-1)
	print (low, high, sum)
	F = open('tesla.txt', 'r')
	A = array.array('f')
	for line in F:
		A.insert (0, float(line))
	B = differenceArray(A)
	(low, high, sum) = FindMaximumSubarray(B, 0, len(B)-1)
	print (low, high, sum)
	F = open('samsung.txt', 'r')
	A = array.array('f')
	for line in F:
		A.insert (0, float(line))
	B = differenceArray(A)
	(low, high, sum) = FindMaximumSubarray(B, 0, len(B)-1)
	print (low, high, sum)

if __name__ == "__main__":
	main()
