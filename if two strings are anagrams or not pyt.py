
def check(S , T):
	if(sorted(S)== sorted(T)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")		
		

S = str(input('enter the first string: '))
T = str(input('enter the second string: '))
check(S , T)
