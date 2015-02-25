from collections import defaultdict
import math

def anagram(string1,string2):
	if (sorted(string1) == sorted(string2)):
		return True
	else:
		return False

def anagramSet(list1):
	# itemset = defaultdict(list)
	itemset = {}
	result = []
	for x in range(0,len(list1)):
		key = ''.join(sorted(list1[x]))
		# print itemset
		if key in itemset:
			itemset[key].append((list1[x]))
		else:
			itemset[key] = [list1[x]]

	# itemset =  sorted(itemset)
	# itemsetKeys = sorted(itemset)
	# for x in itemset.keys():
	for x in (sorted(itemset)):
		result.append(itemset[x])
	# print itemsetKeys
	# print itemset
	return result

def anagramQuestion(list1, input):
	dict1 = {}
	for x in range(0,len(list1)):
		key = ''.join(sorted(list1[x]))
		if key in dict1:
			dict1[key].append(list1[x])
		else:
			dict1[key] = [list1[x]]
	result = []
	for x in dict1:
		inputsorted = ''.join(sorted(input))
		if x == inputsorted:
			dict1[x].remove(input)
			result.append(dict1[x])

	return result

def closestPoints(list1,list2,n):
	x = list2[0][0]
	y = list2[0][1]
	dist = {}
	result = []
	for i in range(0,len(list1)):
		x1 = list1[i][0]
		y1 = list1[i][1]
		distance = round((math.sqrt(((x-x1)** 2)+((y-y1) ** 2))),3)
		# distance = round(distance,3)
		if distance in dist:
			dist[distance].append(list1[i])
		else:
			dist[distance] = [list1[i]]

	# print dist
	for k in sorted(dist):
		result.append(dist[k])

	return result[0:n]


if __name__ == '__main__':
	# if(anagram('cars','arcs')):
	# 	print "cars and arcs are anagram"
	# else:
	# 	print "no they are not!" 
	# print(anagramSet(['cars','steer','bike','arcs','trees']))

	print(closestPoints([(-2,-4),(0,0),(10,15),(5,6),(7,8),(-10,-30)],[(5,5)],2))
	# print(anagramQuestion(['cat','good','tac','act'],'tac'))
	
