#Joshua Rinaldi
#101902285
#9/24/14
#HW5

import math
import array
import time

class NODE:
	def __init__(self):
		self.orig = ''
		self.key = []
		self.possibles = []
		self.next = []
		self.head = True

def buildNodes(word):
	A = NODE()
	A.orig = word
	A.key = sorted(list(word))
	for k in range(0 , len(word)):
		newWord = word.replace(word[k], '', 1)
		A.possibles.append(newWord)
	return A

def makeMatrix(iFile):
	words = iFile.readlines()
	words = map(lambda s: s.strip(), words)
	Length = 0
	for i in words:
		if (len(i) > Length):
			Length = len(i)
	matrix = []
	for j in range(Length):
		matrix.append([])
	for q in words:
		node = buildNodes(q)
		matrix[len(q)-1].append(node)
	return matrix

def anagram(a, b):
	if (sorted(list(a)) == sorted(list(b))):
		return 1
	else:
		return 0

def makeDag(matrix):
	dag = []
	for i in range (1, len(matrix)):
		for j in range (0, len(matrix[i])):
			dag.append(matrix[i][j])
			for v in range(0, len(matrix[i][j].possibles)):
				for q in range(0, len(matrix[i-1])):
					if (anagram(matrix[i][j].possibles[v], matrix[i-1][q].key)):
						matrix[i-1][q].next.append(matrix[i][j])
						matrix[i][j].head = False
	return dag

def DFSrecurse(node, path, pathMatrix):
	path.append(node)
	if (len(node.next) == 0):
		newPath = list(path)
		pathMatrix.append(newPath)
	else:
		for x in node.next:
			DFSrecurse(x, path, pathMatrix)
	path.pop()

def dfs(node):
	path = []
	pathMatrix = []
	DFSrecurse (node, path, pathMatrix)
	return pathMatrix

def main():
	name = raw_input('please type the name of the Input File: ')
	iFile = open(name, 'r')
	matrix = makeMatrix(iFile)
	#print (matrix)
	#for i in range(0, len(matrix)):
	#	for j in range(0, len(matrix[i])):
	#		print (matrix[i][j].possibles)
	dag = makeDag(matrix)
	headList = []
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[i])):
			if (matrix[i][j].head == True):
				headList.append(matrix[i][j]) 
	finalPath = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
	for i in headList:
		x = dfs(i)
		finalPath[len(x)].append(x)
	for i in range(0, len(finalPath)-1):
		if (len(finalPath[i+1]) == 0):
			for j in range(0, len(finalPath[i])):
				for k in range(0, len(finalPath[i][j])):
					for l in range (0, len(finalPath[i][j][k])):
						print finalPath[i][j][k][l].orig, '->', 
					print ''

if __name__ == "__main__":
    main()
