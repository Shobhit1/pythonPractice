import math

def findMax(array):
	max = array[0];
	for i in range(0,len(array)):
		if (array[i] >= max):
			max = array[i]
			# print max
	return max

def countingSort(A):
	k = findMax(A)
	count = [0] * (k+1)

	for j in range(len(A)):
		count[A[j]] = count[A[j]]+1

	# print count

	for x in range (1,len(count)):
		count[x] = count[x-1] + count[x]

	return count

def sort(A):
	output = [0]*(len(A)+1)
	# print output
	count = countingSort(A)
	for l in range(0,len(A)):
		output[count[A[l]]] = A[l]
		count[A[l]] = count[A[l]] - 1
	# print output
	# return count
	return output[1:]

def majorityElement(array):
	n = len(array)
	# print n
	# majorityElement = 0
	occurance = int((math.ceil(n/2))+1)
	# print occurance
	k = findMax(array)
	count = [0]*(k+1)
	for j in range(len(array)):
		count[array[j]] = count[array[j]] + 1
	print count
	for i in range(0,len(count)):
		# print count[i]
		if count[i] >= occurance:
			majorityElement = i
	return majorityElement

def median(array):
	tempList = []
	tempList = countingSort(array)
	n = len(tempList)
	if (n%2==0):
		median = (tempList[(n/2)-1] + tempList[n/2])/2
	else:
		median = tempList[n/2]
	return median

if __name__ == '__main__':
	array1 = [3,3,2,4,1,4,11,6,3,2,1,4,7,9,2,4,5,7,3,4,8,9,3,4]
	# print(findMax(array1))
	# output = []*len(array1)
	# print(countingSort(array1))
	# print(median(array1))
	print majorityElement(array1)