
def computeHCF(num1 ,num2):

  if num1> num2:
      smaller = num2
  else:
      smaller = num1

  for i in range(1, smaller+1):
      if((num1 % i == 0) and (num2 % i == 0)):
          hcf = i

  return hcf

num1 = int(input('num1: '))
num2 = int(input('num2: '))

print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))
