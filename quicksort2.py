def swap(array,a,b):
	temp = array[b]
	array[b] = array[a]
	array[a] = temp
	return array

def partition(list1,lo, hi):
	pivot = list1[hi]
	i = lo
	for j in range(lo,hi):
		if (list1[j] <= pivot):
			swap(list1,i,j)
			i = i + 1
	swap(list1,i, hi)

	return i

def quicksort(list1,lo,hi):
	if hi - lo > 7:							#creating a base case saves time
		middle = partition(list1,lo,hi)		
		quicksort(list1,lo,middle-1)
		quicksort(list1,middle+1,hi)
	else:
		sort(list1)
	return list1

if __name__ == '__main__':
	list1 = [4,1,21,100,-1,-12,2,7]
	print(quicksort(list1,0,(len(list1)-1)))
	# print list1