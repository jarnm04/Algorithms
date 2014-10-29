#Joshulength Rinaldi
#101902285
#10/28/14
#HW7
#Sources used: http://vlsicad.ucsd.edu/courses/cse101-w14/hw/hw4_solutions.pdf

import string
import array
import sys

def findMax(i, j, price, money):
	maxA = 0
	maxB = 0
	for a in range (0, i):
		temp = money[a][j] + money[i-a][j] 
		if (temp > maxA):
			maxA = temp
	for b in range (0, j):
		temp = money[i][j-b] + money[i][b]
		if (temp > maxB):
			maxB = temp
	maxPrice = price[i][j]
	if ((maxA > maxB) and (maxA > maxPrice)):
		return maxA
	elif ((maxB > maxB) and (maxB > maxPrice)):
		return maxB
	else:
		return maxPrice

def maxMoney(i, j, price, money):
	if (money[i][j] != -1):
		return money[i][j]
	else:
		money[i][j] = findMax(i, j, price, money)
		return money[i][j]


def main():
	fileName = sys.argv[-1]
	iFile = open(fileName, 'r')
	XY = []
	patterns = 0
	possibles = []
	for i, line in enumerate(iFile):
		Input = line.strip()
		if (i == 0):
			xDim = ''
			yDim = ''
			spaces = 0
			for j in range (0, len(Input)):
				if (Input[j] == ' '):
					spaces += 1
				elif (spaces == 0):
					xDim += Input[j]
				elif (spaces == 1):
					yDim += Input[j]
			XY.append(int(xDim))
			XY.append(int(yDim))
		elif (i == 1):
			patterns = int(Input)
		elif (Input != ''):
			smallX = ''
			smallY = ''
			profit = ''
			spaces = 0
			for i in range (0, len(Input)):
				if (Input[i] == ' '):
					spaces += 1
				elif (spaces == 0):
					smallX += Input[i]
				elif (spaces == 1):
					smallY += Input[i]
				elif (spaces == 2):
					profit += Input[i]
			profitArray = []
			profitArray.append(int(smallX))
			profitArray.append(int(smallY))
			profitArray.append(int(profit))
			possibles.append(profitArray)

	print possibles

	price = []
	money = []

	for i in range (0, XY[0]):
		price.append([])
		money.append([])
		for j in range (0, XY[1]):
			price[i].append([])
			money[i].append([])

	for i in range (1, XY[0]):
		for j in range (1, XY[1]):
			price[i][j] = -1

	for i in range (1, patterns):
		cur = possibles[i]
		if (price[cur[0]-1][cur[1]-1] < possibles[i][2]):
			price[cur[0]-1][cur[1]-1] < possibles[i][2]

	for i in range (0, XY[1]):
		for j in range (0, XY[1]):
			money[i][j] = -1

	money[0][0] = 0

	for i in range(0, XY[0]):
		for j in range(0, XY[1]):
			maxMoney(i, j, price, money)




if __name__ == "__main__":
    main()