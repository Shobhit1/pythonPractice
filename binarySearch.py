def binarySort(A,taget):
	lo = 1;
	high = len(A);
	# print lo,high
	while lo <=  high:
		mid = int(lo+(high-lo)/2)
		# print mid
		if (A[mid] == taget):
			return mid
			# print "in if"
		if (A[lo] <= A[mid]):
			if (A[mid] < taget):
			lo = mid + 1
			# print "in elif"
		else:
			high = mid - 1
			# print "in else"
	
if __name__ == '__main__':
	array = [0,5,13,19,22,41,55,68,72,81,98,99]
	print (binarySort(array,13))