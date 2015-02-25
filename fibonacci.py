def fibonacci(list1,n):
	for i in range(2,11):
		list1.append(list1[i-1] + list1[i-2])
		# list1.append(listElement)
	return list1


def wordCount(list1):
	# temp = []
	for x in range(0,len(list1)):
		list1[x] = list1[x].upper()

	dict1 = {}

	for x in range(0,len(list1)):
		if list1[x] in dict1:
			dict1[list1[x]].append(x)
		else:
			dict1[list1[x]] = [x]


	for key in dict1:
		print key.capitalize(), " - " , len(dict1[key])

if __name__ == '__main__':
	
	list2 = ['Good','word','good','woRd']
	(wordCount(list2))
	# print(fibonacci([0,1],))