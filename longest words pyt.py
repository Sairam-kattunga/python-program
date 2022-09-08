
def longestLength(a):
	max1 = len(a[0])
	temp = a[0]

	for i in a:
		if(len(i) > max1):

			max1 = len(i)
			temp = i

	print("The word with the longest length is:", temp)
p = input('enter the firstt word: ')
q = input('enter the firstt word: ')

r = input('enter the firstt word: ')

s = input('enter the firstt word: ')





a = [p, q, r, s]
longestLength(a)
