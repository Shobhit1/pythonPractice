def binaryRotated(A,target,lo,high):
	# lo = 1
	# high = len(A)

	if (lo>high):
		return -1

	mid = lo + (high-lo)/2

	if (A[mid] == target):
		return mid

	if (A[lo] <= A[mid]):
		if ((A[lo] <= target)and(target <= A[mid])):
			return binaryRotated(A,target,lo,mid-1)
		else:
			return binaryRotated(A,target,mid+1,high)

	else:
		if((target >= A[mid]) and (target<=A[high])):
			return binaryRotated(A,target,mid+1,high)
		else:
			return binaryRotated(A,target,lo,mid-1)


if __name__ == '__main__':
	array = [19, 20, 21, 25, 30, 35, 1, 2, 3, 4]
	print (binaryRotated(array,21,0,len(array)-1))