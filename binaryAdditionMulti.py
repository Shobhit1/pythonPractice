# def binaryAddition(num1,num2):
	
# 	num1_dec = int(num1,2)
# 	num2_dec = int(num2,2)

# 	sum1 = num1_dec+num2_dec
# 	return (bin(sum1)[2:])

# if __name__ == '__main__':
# 	# num1 = raw_input("Enter first binary")
# 	# num2 = raw_input("Enter second binary")
# 	print(binaryAddition('101','11001'))


# def lengthOfsum1(num1,num2):
# 	if len(num1) > len(num2):
# 		length = len(num1)
# 	elif len(num1) < len(num2):
# 		length = len(num2)
# 	else:
# 		if (num1[len(num1)-1] == num2[len(num2)-1] == 1):
# 			length = len(num1) + 1
# 		else:
# 			length = len(num1)

# 	return length

def addCheck(num1,num2,carry):
	sum1 = '0'
	# carry = '0'
	if (num1== '1' and num2 == '1' and carry == '0'):
		sum1 = '0'
		carry = '1'
		return (sum1,carry)
	if (num1 == '1' and num2 == '1' and carry == '1'):
		sum1 = '1'
		carry = '1'
		return (sum1,carry)
	if (num1 == '0' and num2 == '0' and carry == '0'):
		sum1 = '0'
		carry = '0'
		return (sum1,carry)
	if (num1 == '0' and num2 == '0' and carry == '1'):
		sum1 = '1'
		carry = '0'
		return (sum1,carry)
	if (num1 == '1' and num2 == '0' and carry == '0'):
		sum1 = '1'
		carry = '0'
		return (sum1,carry)
	if (num1 == '1' and num2 == '0' and carry == '1'):
		sum1 = '0'
		carry = '1'
		return (sum1,carry)
	if (num1 == '0' and num2 == '1' and carry == '0'):
		sum1 = '1'
		carry = '0'
		return (sum1,carry)
	if (num1 == '0' and num2 == '1' and carry == '1'):
		sum1 = '0'
		carry = '1'
		return (sum1,carry)

	# print "sum and carry are " + sum1 + " " + carry
	# return (sum1,carry)

def binaryAddition(num1,num2):

	# num1Int = [0]*len(num1)
	# num2Int = [0]*len(num2)
	# # print num1Int
	# # print num2Int
	# for i in range(0,len(num1)):
	# 	num1Int[i] = int(num1[i])

	# for j in range(0,len(num2)):
	# 	num2Int[j] = int(num2[j])

	# num1Int.reverse()
	# num2Int.reverse()

	# print num1Int
	# print num2Int

	# lengthsum1 = lengthOfsum1(num1,num2)
	# print lengthsum1
	
	sum1 = []
	# carry = 0
	# print sum1
	i = len(num1) - 1
	j = len(num2) - 1
	carry = '0'
	while (i >= 0 and j >= 0):
		# carry = '0'
		# print num1[len(num1)-x]
		# print num2[len(num2)-x]
		# print carry
		# if((num1[len(num1)-x] == '0') and (num2[len(num2)-x] == '0')):
		# 	if (carry >= 1):
		# 		sum1.append(1)
		# 	else:
		# 		sum1.append(0)
		# elif((num1[len(num1)-x] == '1') and (num2[len(num2)-x] == '1')):
		# 	if (carry >= 1):
		# 		sum1.append(1)
		# 		carry = carry + 1
		# 	else:
		# 		sum1.append(0)
		# 		carry = carry + 1
		# 	# print carry
		# else:
		# 	if (carry >= 1):
		# 		sum1.append(0)
		# 		carry = carry + 1
		# 	else:
		# 		sum1.append(1)

		# print num1[i]
		# print "Adding " + num1[i] + "and " + num2[j] + "and carry " + carry
		sum1temp,carry = addCheck(num1[i],num2[j],carry)
		# print "sum and carry " + sum1temp + " " + carry
		i = i-1
		j = j-1
		# print sum1temp
		sum1.append(sum1temp)
		# print sum1
		# print carry


	if i >= 0:
		while (i>=0):
			sum1temp,carry = addCheck(num1[i],carry,'0')
			sum1.append(sum1temp)
			i = i - 1

	if j >= 0:
		while(j>=0):
			sum1temp,carry = addCheck(num2[j],carry,'0')
			sum1.append(sum1temp)
			j = j - 1

	if (carry == '1'):
		sum1.append('1')

	# print sum1

	sum1.reverse()

	return sum1

	# sum1.reverse()
# 
	# print sum1

def multCheck(num1, num2):
	# print "num1 " + num1 + " num2 " + num2
	if (num1 == '1' and num2 == '1'):
		return '1'
	else:
		return '0'

def multiply(num1, num2):
	list1 = []
	
	j = len(num2)-1

	while(j>=0):
		str1 = ''
		i = len(num1)-1
		while (i>=0):
			str1 = multCheck(num2[j],num1[i]) + str1
			i = i-1
		str1 = str1+('0'* (len(num2)-1-j))
		# list1.append(str1)
		# print "str1 " + str1
		j = j-1
		list1.append(str1)
	
	# l = 0
	result = []
	# print "before while"
	# while():
	for l in range(0,len(list1)-1):
		# print l
		result = binaryAddition(list1[l],list1[l+1])
		# print result
		# l = l + 1
	# result.reverse()

	return result

	# print list1



if __name__ == '__main__':
	# print(binaryAddition('1100','11000'))
	print(multiply('110','110'))
